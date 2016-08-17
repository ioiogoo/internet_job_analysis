from . import db
from peewee import *

class City(db.model):
	"""docstring for City"""
	class Meta:
		db_table = 'city'

	id = PrimaryKeyField()
	