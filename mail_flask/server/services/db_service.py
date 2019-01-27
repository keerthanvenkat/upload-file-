import pymysql


class DBConnect:
    def __init__(self, hname, uname, pwd, dbname, port = 3306):
        self.task_db_host = hname
        self.TASK_DB_USERNAME = uname
        self.TASK_DB_PASSWORD = pwd
        self.TASK_DATABASE_NAME = dbname
        self.TASK_DB_PORT = port
        self._cursor = None

        self._connection = pymysql.connect(self.task_db_host, self.TASK_DB_USERNAME, self.TASK_DB_PASSWORD,
                                           self.TASK_DATABASE_NAME, self.TASK_DB_PORT)

    def begin(self):
        assert self._connection is not None
        assert self._cursor is not None
        self._cursor = self._connection.cursor()
        return self._cursor

    def commit(self):
        assert self._connection is not None
        assert self._cursor is not None
        self._cursor.close()
        self._connection.commit()
        self._cursor = None

    def close(self):
        if self._connection is not None:
            self._connection.close()
            self._connection = None

    def rollback(self):
        assert self._connection is not None
        assert self._cursor is not None
        self._cursor.close()
        self._cursor = None


    def execute(self, query, param = None):
        cursor = self._cursor
        assert cursor is not None
        try:
            if type(param) is tuple:
                cursor.execute(query, param)
            elif type(param) is list:
                cursor.execute(query, param)
            else:
                cursor.execute(query)
            return True
        except Exception as e:
            raise e

    def execute_insert(self, query, param):
        cursor = self._cursor
        assert cursor is not None
        try:
            if type(param) is tuple:
                cursor.execute(query, param)
            elif type(param) is list:
                cursor.execute(query, param)
            else:
                cursor.execute(query)
            no = len(cursor.lastrowid)
            if no == 0:
                return False
            else:
                return no
        except Exception as e:
            raise e

    def select_all(self,query, param=None):
        cursor = self._cursor
        assert cursor is not None
        try:
            if param is None:
                cursor.execute(query)
            else:
                if type(param) is tuple:
                    cursor.execute(query, param)
                elif type(param) is list:
                    cursor.execute(query, param)
                else:
                    cursor.execute(query)
            res = cursor.fetchall()
            # cursor.nextset()
            return res
        except Exception as e:
            raise e

    def select_one(self, query, param =None):
        cursor = self._cursor
        assert cursor is not None
        try:
            if param is None:
                cursor.execute(query)
            else:
                if type(param) is tuple:
                    cursor.execute(query, param)
                elif type(param) is list:
                    cursor.execute(query, param)
                else:
                    cursor.execute(query)
            res = cursor.fetchone()
            return res
        except Exception as e:
            raise e

    def bulk_insert(self,table, columns, valueList):
        # stringValue = []
        # for i in
        pass

    def delete(self,table,condition, condition_val):
        query  ="DELETE from " +table +" WHERE " +condition
        try:
            return self.execute(query, condition_val)
        except Exception as e:
            raise e


