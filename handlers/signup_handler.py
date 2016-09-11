from basic_handler import *
from general import * 

class SignupHandler(Handler) :
	def get(self) :
		self.render("signup.html")

	def post(self) :
		# getting data from form
		username = self.request.get("username")
		password = self.request.get("password")
		verify = self.request.get("verify")
		email = self.request.get("email") 
		# error variables
		error_username = ""
		error_password = ""
		error_verify = ""
		error_email = ""
		# flag for errors
		cond_error = False
		if not self.validate_user(username) :
			error_username = "That's not a Valid User"
			cond_error = True
		if not self.validate_password(password):
			error_password = "That's not a Valid Password"
			cond_error = True
		else :
			if password != verify :
				error_verify = "Your passwords didn't match."
				cond_error = True
		if email :
			if not self.validate_email(email) :
				error_email = "That's not a Valid Email"
				cond_error = True

		if cond_error == False :
			self.write("Bienvenido")
		else :
			self.render("signup.html",
							error_username= error_username, 
							error_password = error_password,
							error_verify = error_verify,
							error_email = error_email, 
							username = username, 
							email = email,
							)

	# validates functions
	def validate_user(self, usuario) :
		return user_check.match(usuario)

	def validate_password(self, password) :
		return password_check.match(password)

	def validate_email(self, email) :
		return email_check.match(email)