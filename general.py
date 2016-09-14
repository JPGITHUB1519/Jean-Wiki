# this saves all the globals variables
import re
import random
import string
import hashlib 
import logging
from google.appengine.ext import db
from google.appengine.ext import ndb # I don't use db model
from models.wiki_post import WikiPost
from models.wiki_post_version import WikiPostVersion

# validation variables
user_check = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
password_check = re.compile(r"^.{3,20}$")
email_check = re.compile(r"^[\S]+@[\S]+.[\S]+$")


