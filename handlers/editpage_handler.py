from basic_handler import *

class EditPageHandler(Handler) :
	def get(self, url) :
		self.write(url)