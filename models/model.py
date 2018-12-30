import sqlite3
import os

class model():
	def create(self):
		conn = sqlite3.connect('tacobro.db')
		cur = conn.cursor()
		classname = type(self).__name__
		querystring="INSERT INTO " + classname +"("
		parameter=()
		kwargs = self.__dict__
		for arg in kwargs:
			querystring+=arg+", "
			parameter+=(str(kwargs[arg]),)
		querystring=querystring[:-2]
		querystring+=") "
		querystring+= " VALUES ("
		for i in range(len(kwargs)):
			if i==(len(kwargs)-1):
				querystring+="?)"
			else:
				querystring+="?, "
		cur.execute(querystring, parameter)
		conn.commit()
		cur.close()
		conn.close()

