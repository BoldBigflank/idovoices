from google.appengine.ext import db

class User(db.Model):
    number = db.PhoneNumberProperty()
    score = db.IntegerProperty(default=0)
    word = db.StringProperty(verbose_name=None, multiline=False)