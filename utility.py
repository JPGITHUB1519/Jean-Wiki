# this have all the utilities methods
import sys
sys.path.append("../")
import random
import string
import re
import general
import hashlib
import logging
from google.appengine.ext import db
from google.appengine.ext import ndb # I don't use db model
# import memchache
from google.appengine.api import memcache
import models.wiki_post
import models.wiki_post_version

ancestor_key = ndb.Key("WikiPost", "parents")
SECRET = "PYTHON"
# User System function
def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

# make password hash
def generate_hash(name, pw, salt) :
	return hashlib.sha256(name + pw + salt).hexdigest()

# this is the method to generate a hash to the user and password
def make_password_hash(name, pw):
    salt = make_salt()
    h = generate_hash(name, pw, salt)
    return '%s,%s' % (h, salt)

# verify if hash mash with a user 
def valid_password(name, pw, h):
    obtain_salt = h.split(',')[1]
    test_h = generate_hash(name, pw, obtain_salt) + "," + obtain_salt
    if  test_h == h :
    	return True
    return False

# cookie hashing
def hash_str(s):
	# simuling hmac
    return hashlib.sha256(s + SECRET).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    lista = h.split('|')
    if hash_str(lista[0]) == lista[1] :
    	return lista[0]
    return None

# caching
# looks for the post in the cache or in the database remember that url is unique
def get_wiki_post(url, update = False) :
    key = str(url)
    # looking for the url in the cache
    wiki_posts = memcache.get(key)
    # if the post was not in the cache or it has to update
    if not wiki_posts or update :
        logging.error("DBQUERY")
        # making the query in the database
        wiki_posts = models.wiki_post.WikiPost.query(ancestor = ancestor_key).filter(models.wiki_post.WikiPost.url == url).get()
        memcache.set(key, wiki_posts)
    return wiki_posts

# I save the version in the cache with the sufix "v" + url(v/1)
def get_wiki_version(v, update = False) :
    sufix = "v"
    key = sufix + str(v)
    # get version
    # converting url to key
    v_key = ndb.Key(urlsafe= v)
    # converting key to id and getting value by id 
    # if there is a version we assign the version to the post else assign post
    wiki_version = memcache.get(key)
    if not wiki_version or update :
        logging.error("Single Version Query")
        wiki_version = models.wiki_post_version.WikiPostVersion.get_by_id(v_key.id(), parent = ancestor_key)
        memcache.set(key, wiki_version)
    return wiki_version