from basic_handler import *
from models.wiki_post import WikiPost
from google.appengine.ext import db

class EditPageHandler(Handler) :
	# parameter url is for get in the url
	def get(self, url) :
		post = WikiPost.query(ancestor = ancestor_key).filter(WikiPost.url == url).get()
		# if the post exits load the content of the post and assign it to the textarea
		if post :
			self.render("edit_page.html", post_value = post.content)
		else :
			self.render("edit_page.html")

	def post(self, url) :
		# saving wiki post in database
		post = self.request.get("wikipost")
		postobj = WikiPost(parent = ancestor_key, url = url, content = post)
		postobj.put()
		# redirecting post to the page
		self.redirect(url)