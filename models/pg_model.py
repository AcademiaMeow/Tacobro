import psycopg2
import os


class pg_model():
	def create(self):
		conn = psycopg2.connect('tacobro.db')
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
				querystring+="%s)"
			else:
				querystring+="%s, "
		cur.execute(querystring, parameter)
		cur.close()
		conn.close()
