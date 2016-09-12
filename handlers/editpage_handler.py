from basic_handler import *
from models.wiki_post import WikiPost
from google.appengine.ext import db

class EditPageHandler(Handler) :
	# parameter url is for get in the url
	def get(self, url) :
		#self.write(url)
		self.render("edit_page.html")

	def post(self, url) :
		# saving wiki post in database
		post = self.request.get("wikipost")
		postobj = WikiPost(parent = ancestor_key, url = url, content = post)
		postobj.put()
		# redirecting post to the page
		self.redirect(url)