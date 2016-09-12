from google.appengine.ext import ndb

class WikiPost(ndb.Model) :

	url  = ndb.StringProperty(required = True)
	content = ndb.TextProperty(required = True)
	date = ndb.DateProperty(auto_now_add = True)