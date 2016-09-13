from basic_handler import *
from models.wiki_post import WikiPost
from models.wiki_post_version import WikiPostVersion
import logging

class HistoryPageHandler(Handler) :
	def get(self, url) :
		post_versionobj = WikiPostVersion()
		# getting relation
		list_version = post_versionobj.get_r_post_relation(url)
		
		# Accessing Referenced Values
		#logging.error(i.r_post.get().url)
		self.render("historypage.html", list_version = list_version, url = url)

	def post(self, url):
		pass
