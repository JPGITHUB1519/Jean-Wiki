from basic_handler import *

class WikiPageHandler(Handler) :
	# parameter url is for get in the url
	def get(self, url) :
		self.render("wikipage.html")