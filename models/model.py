from models.pg_model import pg_model
from models.sqlite_model import sqlite_model
import os

class model():
	dao = sqlite_model()
	# dao = pg_model()
	def create(self):
		dao.create(self, self.__name__)

class Q():
	AND=0
	OR=1
	def __init__(self, **kwargs):
		self.querystring=""
		self.parameter=()
		if len(kwargs) == 1:
			for arg in kwargs:
				self.querystring=arg+" = ?"
				self.parameter=(str(kwargs[arg]),)

	def add(self, q, op):
		if op == 0:
			op_str = "AND"
		elif op == 1:
			op_str = "OR"
		self.querystring+=" "+op_str+" "
		self.querystring+=q.querystring
		self.parameter+=(q.parameter)
