#This is the place where all URL mapping goes

# importing handlers
from handlers import *
route_list = [('/', main_handler.MainHandler),
			  ("/login", login_handler.LoginHandler),
			  ("/signup", signup_handler.SignupHandler)]