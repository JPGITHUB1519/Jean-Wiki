# this saves all the globals variables
import re
import random
import string
import hashlib 
import logging
from google.appengine.ext import db
from google.appengine.ext import ndb # I don't use db model
from models.wiki_post import WikiPost
from models.wiki_post_version import WikiPostVersion

# import memchache
from google.appengine.api import memcache
# validation variables
user_check = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
password_check = re.compile(r"^.{3,20}$")
email_check = re.compile(r"^[\S]+@[\S]+.[\S]+$")

# SECRET FOR COOKIES

SECRET = "PYTHON"

# parents for post
ancestor_key = ndb.Key("WikiPost", "parents")

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
		wiki_posts = WikiPost.query(ancestor = ancestor_key).filter(WikiPost.url == url).get()
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
		wiki_version = WikiPostVersion.get_by_id(v_key.id(), parent = ancestor_key)
		memcache.set(key, WikiPost)
	return wiki_version


