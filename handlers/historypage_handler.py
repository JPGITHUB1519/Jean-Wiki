from basic_handler import *

class HistoryPageHandler(Handler) :
	def get(self, url) :
		self.render("historypage.html")

	def post(self, url):
		pass
