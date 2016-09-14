from basic_handler import *
from models.wiki_post import WikiPost
from models.wiki_post_version import WikiPostVersion
from google.appengine.ext import db
import time

class WikiPageHandler(Handler) :
	# parameter url is for get in the url
	def get(self, url) :
		# for get if any version
		v = self.request.get("v")
		# if the version is passed on the get parameter
		if v :
			# get version
			# converting url to key
			v_key = ndb.Key(urlsafe= v)
			# converting key to id and getting value by id 
			# if there is a version we assign the version to the post else assign post
			post = WikiPostVersion.get_by_id(v_key.id(), parent = ancestor_key)
		else :
			# get post	
			post = WikiPost.query(ancestor = ancestor_key).filter(WikiPost.url == url).get()
		# if the user is logged
		if self.user :
			# get url
			if post :
				# if version is, send version key on url
				if v :
					self.render("wikipage.html", post = post.content, url = post.r_post.get().url, access = True, version = v)
				else :
					# send url for edit if the user wants
					# send access for know if the user is logged
					self.render("wikipage.html", post = post.content, url = post.url, access = True)
			else :
				#if the post do not exits redirect to edit_
				self.redirect('/_edit' + url)
		else :
			# if the user do not exits only see
			if post : 
				self.render("wikipage.html", post = post.content, access = False)
			else :
				#if the post do not exits, see the 404 page
				self.render("404.html")
