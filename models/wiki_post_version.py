from wiki_post import WikiPost
from google.appengine.ext import ndb
import sys
import logging
# adding to the sys the path parent to import the files
sys.path.append("../")
from general import *
from utility import *
from google.appengine.api import memcache

class WikiPostVersion(ndb.Model) :
	r_post = ndb.KeyProperty(kind = WikiPost)
	content = ndb.StringProperty()
	date = ndb.DateProperty(auto_now_add = True)

	# this method return all the relations of wikipostversion to WikiPostVersion
	# postobj = objeto
	# (inner join XD)  
	# return all the post versions that macht with post
	def get_r_post_relation(self, url, update = False) :
		ancestor_key = ndb.Key("WikiPost", "parents")
		sufix = "r"
		key = sufix + url
		list_version = memcache.get(key)
		if not list_version or update :
			logging.error("LIST VERSION QUERY")
			postobj = get_wiki_post(url)
			list_version = WikiPostVersion.query().filter(WikiPostVersion.r_post == postobj.key)
			memcache.set(key, list_version)
		return list_version

