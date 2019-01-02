import psycopg2
import os

# TODO Fix


class pg_model():
    def create(self, classname, **kwargs):
        user = os.environ['Postgres_USER']
        host = os.environ['Postgres_HOST']
        password = os.environ['Postgres_PWD']
        conn_str = "dbname='tacobro' user='%s' host='%s' " + \
            "password='%s'"
        conn = psycopg2.connect(conn_str)
        cur = conn.cursor()
        querystring = "INSERT INTO " + classname + " ("
        parameter = ()
        for arg in kwargs:
            querystring += arg + ", "
            parameter += (str(kwargs[arg]),)
        querystring = querystring[:-2]
        querystring += ") "
        querystring += " VALUES ("
        for i in range(len(kwargs)):
            if i == (len(kwargs) - 1):
                querystring += "?)"
            else:
                querystring += "?, "
        cur.execute(querystring, parameter)
        cur.close()
        conn.close()

    def filter(self, classname, q):
        conn = sqlite3.connect('tacobro.db')
        cur = conn.cursor()
        querystring = "SELECT * FROM " + classname
        if not q.querystring == "":
            querystring += " WHERE "
            querystring += q.querystring
            cur.execute(querystring, q.parameter)
            return cur.fetchall()
        else:
            cur.execute()
            return cur.fetchall()

    def filter(self, classname, **kwargs):
        conn = sqlite3.connect('tacobro.db')
        cur = conn.cursor()
        querystring = "SELECT * FROM " + classname
        if not len(kwargs) == 0:
            querystring += " WHERE "
            for arg in kwargs:
                querystring += arg + " = " + "? AND "
                parameter += (str(kwargs[arg]),)
            querystring = querystring[:-4]
            cur.execute(querystring, parameter)
        else:
            cur.execute(querystring)
        return cur.fetchall()
