from basic_handler import *

class LoginHandler(Handler) :
	def get(self) :
		self.render("login.html")