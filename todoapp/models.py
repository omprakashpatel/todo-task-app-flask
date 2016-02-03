from todoapp import app

from mongoengine import *

# Mongo DB instance
connect("todo_app", host="127.0.0.1", port=27017)
# connect(app.config['MONGODB_SETTINGS'])

class Task(Document):
	""" docstring for UrlShortner """
	title = StringField(required=True, max_length=200)
	desc = StringField()
	created_at = StringField()
	updated_at = StringField()
	tags = ListField()
