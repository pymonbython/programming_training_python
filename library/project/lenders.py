from collections import namedtuple
import sqlite3

from db import Database


Entity = namedtuple('Entity', 'name car_model car_return_at')

def get_lenders_by_return_date(connection, car_return_date):
    entities = []
    with Database(connection) as db:
        db.cursor.execute('''
            SELECT name, car_model, car_return_at FROM lender
            WHERE car_return_at <= ?          
        ''', (car_return_date, ))

        for name, car_model, car_return_at in db.cursor.fetchall():
            entities.append(Entity(name, car_model, car_return_at))

    return entities
