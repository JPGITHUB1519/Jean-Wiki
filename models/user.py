from google.appengine.ext import db
class User(db.Model) :
	name = db.StringProperty(required=True)
	password = db.StringProperty(required=True)
	date = db.DateProperty(auto_now_add=True)
