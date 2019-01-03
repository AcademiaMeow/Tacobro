import sqlite3
import os

class sqlite_model():
    """
    @return row id
    """
    def create(self, classname, **kwargs):
        conn = sqlite3.connect('tacobro.db')
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
        id = cursor.lastrowid
        conn.commit()
        cur.close()
        conn.close()
        return id
    """
    @param q is model.Q object
    """
    def filter(self, classname, q):
        conn = sqlite3.connect('tacobro.db')
        cur = conn.cursor()
        querystring = "SELECT * FROM " + classname
        if not q.querystring == "":
            querystring += " WHERE "
            querystring += q.querystring
            cur.execute(querystring, q.parameter)
            data = cur.fetchall()
        else:
            querystring += ";"
            cur.execute(querystring)
            data = cur.fetchall()
        return data
    """
    @param kwargs is key-value filter condition (AND)
    @return key-value
    """
    def filter(self, classname, **kwargs):
        conn = sqlite3.connect('tacobro.db')
        cur = conn.cursor()
        querystring = "SELECT * FROM " + classname
        if not len(kwargs) == 0:
            querystring += " WHERE "
            for arg in kwargs:
                querystring += arg + " = " + "? AND "
                parameter += (str(kwargs[arg]),)
            querystring = querystring[:-4] + ";"
            cur.execute(querystring, parameter)
        else:
            querystring += ";"
            cur.execute(querystring)
        data = cur.fetchall()
        return data
