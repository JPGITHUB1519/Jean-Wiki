from wiki_post import WikiPost
from google.appengine.ext import ndb

class WikiPostVersion(ndb.Model) :
	r_post = ndb.KeyProperty(kind = "WikiPost")
	content = ndb.StringProperty()
	date = ndb.DateProperty(auto_now_add = True)


