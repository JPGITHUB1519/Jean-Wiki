from wiki_post import WikiPost
from google.appengine.ext import ndb
from general import *

class WikiPostVersion(ndb.Model) :
	r_post = ndb.KeyProperty(kind = WikiPost)
	content = ndb.StringProperty()
	date = ndb.DateProperty(auto_now_add = True)

	# this method return all the relations of wikipostversion to WikiPostVersion
	# postobj = objeto
	# (inner join XD)  
	# return all the post versions that macht with post
	def get_r_post_relation(self, url) :
		postobj = WikiPost.query(ancestor = ancestor_key).filter(WikiPost.url == url).get() 
		list_version = WikiPostVersion.query().filter(WikiPostVersion.r_post == postobj.key)
		return list_version

