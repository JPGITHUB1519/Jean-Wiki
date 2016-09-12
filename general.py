# this saves all the globals variables
import re
import random
import string
import hashlib 
from google.appengine.ext import db
from google.appengine.ext import ndb # I don't use db model
# validation variables
user_check = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
password_check = re.compile(r"^.{3,20}$")
email_check = re.compile(r"^[\S]+@[\S]+.[\S]+$")

# SECRET FOR COOKIES

SECRET = "PYTHON"

# parents for post
ancestor_key = ndb.Key("WikiPost", "parents")
