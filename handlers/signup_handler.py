from basic_handler import * 

class SignupHandler(Handler) :
	def get(self) :
		self.render("signup.html")