from google.appengine.ext import db

class Word(db.Model):
    name = db.StringProperty(verbose_name=None, multiline=False)
    lastUse = db.DateTimeProperty(auto_now=True)
