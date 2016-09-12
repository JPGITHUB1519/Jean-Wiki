from basic_handler import * 
from utility import *

class LogoutHandler(Handler) :
	def get(self) :
		self.logout()
