import sqlite3

from  db import Database


with Database(sqlite3.connect('database.db')) as database:
    database.cursor.execute('''
    CREATE TABLE lender(
        id integer primary key autoincrement,
        name text,
        car_model text,
        car_return_at date)
    ''')