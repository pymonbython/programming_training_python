import sqlite3
import os

# from dotenv import load_dotenv, find_dotenv


# load_dotenv(find_dotenv())
# print(os.getenv('FIRST_NAME'))


def create_connection():
    with sqlite3.connect('baza.db') as connection:
        cursor = connection.cursor()
        return cursor

def get_campers_data(cursor):
    cursor.execute('SELECT * FROM campers WHERE marka=?', ('Mercedes-Benz',))
    data = []
    for camper in cursor.fetchall():
        _, marka, model, _ = camper
        data.append({
            'marka': marka,
            'model': model
        })

    return data


if __name__ == '__main__':
    cursor = create_connection()
    models = get_campers_data(cursor)

    print(models)
