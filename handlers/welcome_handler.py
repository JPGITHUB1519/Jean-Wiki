from basic_handler import *
from general import * 
from utility import *
from google.appengine.ext import db
class WelcomeHandler(Handler) :
	def get(self) :
		# checking if is a valid user looged
		if self.user :
			self.render("welcome.html", username = self.user.username)
		else :
			self.redirect("/signup")
		