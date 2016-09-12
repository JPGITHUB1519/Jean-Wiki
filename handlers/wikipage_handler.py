from basic_handler import *
from models.wiki_post import WikiPost
from google.appengine.ext import db
import time

class WikiPageHandler(Handler) :
	# parameter url is for get in the url
	def get(self, url) :
		# new version of ndb
		post = WikiPost.query(ancestor = ancestor_key).filter(WikiPost.url == url).get()
		# if the user is logged
		if self.user :
			# get url
			if post :
				# send url for edit if the user wants
				# send access for know if the user is logged
				self.render("wikipage.html", post = post.content, url = post.url, access = True)
			else :
				#if the post do not exits redirect to edit_
				self.redirect('/_edit' + url)
		else :
			# if the user do not exits only see
			self.render("wikipage.html", post = post.content, access = False)