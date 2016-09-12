from basic_handler import *
from models.wiki_post import WikiPost
from google.appengine.ext import db
import time

class WikiPageHandler(Handler) :
	# parameter url is for get in the url
	def get(self, url) :
		# if the user is logged
		if self.user :
			# get url
			# new version of ndb
			post = WikiPost.query(ancestor = ancestor_key).filter(WikiPost.url == url).get()
			if post :
				self.render("wikipage.html", post = post.content)
			else :
				#if the post do not exits redirect to edit_
				self.redirect('/_edit' + url)
		else :
			self.render("wikipage.html")