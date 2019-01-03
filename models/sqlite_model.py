import sqlite3
import os


class sqlite_model():

    def dict_factory(cursor, row):
        return dict((col[0], row[idx]) for idx, col in enumerate(cursor.description))

    def create(self, classname, **kwargs):
        """
        @return row id
        """
        conn = sqlite3.connect('tacobro.db')
        conn.row_factory = sqlite_model.dict_factory
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
        id = cur.lastrowid
        conn.commit()
        cur.close()
        conn.close()
        return id

    def filter(self, classname, q):
        """
        @param q is model.Q object
        """
        conn = sqlite3.connect('tacobro.db')
        conn.row_factory = sqlite_model.dict_factory
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
        cur.close()
        conn.close()
        return data

    def filter(self, classname, **kwargs):
        """
        @param kwargs is key-value filter condition (AND)
        @return key-value
        """
        conn = sqlite3.connect('tacobro.db')
        conn.row_factory = sqlite_model.dict_factory
        cur = conn.cursor()
        querystring = "SELECT * FROM " + classname
        parameter = ()
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
        cur.close()
        conn.close()
        return data

    def update(self, classname, id, **kwargs):
        """
        @param row id
        """
        conn = sqlite3.connect('tacobro.db')
        cur = conn.cursor()
        querystring = "UPDATE " + classname + "SET "
        parameter = ()
        for arg in kwargs:
            querystring += arg + " = ?, "
            parameter += (str(kwargs[arg]),)
        querystring = querystring[:-2]
        querystring += ") "
        querystring += " WHERE id = ?;"
        parameter += (str(id),)
        cur.execute(querystring, parameter)
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, classname, id):
        """
        @param row id
        """
        conn = sqlite3.connect('tacobro.db')
        cur = conn.cursor()
        querystring = "DELETE FROM " + classname + "WHERE id = ?;"
        cur.execute(querystring, (id,))
        conn.commit()
        cur.close()
        conn.close()
