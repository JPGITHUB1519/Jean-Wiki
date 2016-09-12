from basic_handler import *
from models.wiki_post import WikiPost
from models.wiki_post_version import WikiPostVersion
from google.appengine.ext import db

class EditPageHandler(Handler) :
	# parameter url is for get in the url
	def get(self, url) :
		postobj = WikiPost.query(ancestor = ancestor_key).filter(WikiPost.url == url).get()
		# if the post exits load the content of the post and assign it to the textarea
		if postobj :
			self.render("edit_page.html", post_value = postobj.content)
		else :
			self.render("edit_page.html")

	def post(self, url) :
		post = self.request.get("wikipost")
		# get the first post maching
		postobj = WikiPost.query(ancestor = ancestor_key).filter(WikiPost.url == url).get()
		# if the post exist update it!
		if postobj :
			#updating post
			postobj.content = post
			# adding a new version of the post
			post_versionobj = WikiPostVersion(r_post = postobj.key, content = post)
			post_versionobj.put()
			# adding new post
			postobj.put()
			
			self.redirect(url)	
		else :
			# if the post do not exit saving post in database
			post = self.request.get("wikipost")
			postobj = WikiPost(parent = ancestor_key, url = url, content = post)
			postobj.put()
			# adding a new version of the post
			post_versionobj = WikiPostVersion(parent = ancestor_key, r_post = postobj.key, content = post)
			post_versionobj.put()
			# redirecting post to the page
			self.redirect(url)
			