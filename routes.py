#This is the place where all URL mapping goes

from handlers import *

# condition to newpage
PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'
# importing handlers
from handlers import *
route_list = [('/', main_handler.MainHandler),
			  ("/login", login_handler.LoginHandler),
			  ("/signup", signup_handler.SignupHandler),
			  ("/logout", logout_handler .LogoutHandler),
			  ("/welcome", welcome_handler.WelcomeHandler),
			  ('/_edit' + PAGE_RE, editpage_handler.EditPageHandler),
			  ('/_history' + PAGE_RE, historypage_handler.HistoryPageHandler),
			  (PAGE_RE, wikipage_handler.WikiPageHandler)]