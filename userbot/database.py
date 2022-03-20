import os
import sys
os.system("pip install psycopg2")
import psycopg2

def get_data(self_, key):
    data = self_.get(str(key))
    if data:
        try:
            data = eval(data)
        except BaseException:
            pass
    return data

class SqlDB:
    def __init__(self, url):
        self._url = url
        self._connection = None
        self._cursor = None
        try:
            self._connection = psycopg2.connect(dsn=url)
            self._connection.autocommit = True
            self._cursor = self._connection.cursor()
            self._cursor.execute("CREATE TABLE IF NOT EXISTS UserBot ()")
        except Exception as error:
            if self._connection:
                self._connection.close()
            sys.exit()
        self.re_cache()

    @property
    def name(self):
        return "SQL"

    @property
    def usage(self):
        self._cursor.execute(
            "SELECT pg_size_pretty(pg_relation_size('UserBot')) AS size"
        )
        data = self._cursor.fetchall()
        return int(data[0][0].split()[0])

    def re_cache(self):
        self._cache = {}
        for key in self.keys():
            self._cache.update({key: self.get_key(key)})

    def keys(self):
        self._cursor.execute(
            "SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name  = 'UserBot'"
        )  # case sensitive
        data = self._cursor.fetchall()
        return [_[0] for _ in data]

    def ping(self):
        return True

    def get_key(self, variable):
        if variable in self._cache:
            return self._cache[variable]
        get_ = get_data(self, variable)
        self._cache.update({variable: get_})
        return get_

    def get(self, variable):
        try:
            self._cursor.execute(f"SELECT (%s) FROM UserBot", (str(variable),))
        except psycopg2.errors.UndefinedColumn:
            return None
        data = self._cursor.fetchall()
        if not data:
            return None
        if len(data) >= 1:
            for i in data:
                if i[0]:
                    return i[0]

    def set_key(self, key, value):
        try:
            self._cursor.execute(
                f"ALTER TABLE UserBot DROP COLUMN IF EXISTS (%s)", (str(key),)
            )
        except (psycopg2.errors.UndefinedColumn, psycopg2.errors.SyntaxError):
            pass
        except BaseException as er:
            LOGS.exception(er)
        self._cache.update({key: value})
        self._cursor.execute(f"ALTER TABLE UserBot ADD (%s) TEXT", (str(key),))
        self._cursor.execute(
            f"INSERT INTO UserBot (%s) values (%s)", (str(key), str(value))
        )
        return True

    def del_key(self, key):
        if key in self._cache:
            del self._cache[key]
        try:
            self._cursor.execute(f"ALTER TABLE UserBot DROP COLUMN (%s)", (str(key),))
        except psycopg2.errors.UndefinedColumn:
            return False
        return True

    delete = del_key

    def flushall(self):
        self._cache.clear()
        self._cursor.execute("DROP TABLE UserBot")
        self._cursor.execute("CREATE TABLE IF NOT EXISTS UserBot ()")
        return True

    def rename(self, key1, key2):
        _ = self.get_key(key1)
        if _:
            self.del_key(key1)
            self.set_key(key2, _)
            return 0
        return 1
