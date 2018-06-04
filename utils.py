import sqlite3
import json
from time import gmtime, strftime

def log(level, title, message, more=""):
	with open('logs.json') as f:
		logs = json.load(f)

	logs["logs"].insert(0, { "time" : strftime("%H:%M:%S", gmtime()), "level" : level, "title" : title, "message" : message, "more" : more })

	with open('logs.json', 'w') as f:
		json.dump(logs, f, indent=4)

class Database:
    def __init__(self, name=None):
        self.conn = None
        self.cursor = None
        if name:
            self.open(name)

    def open(self,name):
        try:
            self.conn = sqlite3.connect(name);
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Error connecting to database!")

    def close(self):
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        self.close()

    def get(self, table, columns, limit=None):
        query = "SELECT {0} from {1};".format(columns, table)
        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        return rows[len(rows)-limit if limit else 0:]
    
    def insert(self, table, columns, data):
        query = "INSERT INTO {0} ({1}) VALUES ({2});".format(table, columns, data)
        self.cursor.execute(query)

    def execute(self,sql):
        self.cursor.execute(sql)
        if self.conn:
            self.conn.commit()
