import sqlite3

import pytest

from main import get_campers_data


@pytest.fixture
def create_db():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE campers (id integer, marka text, model text, created_at date)')
    sample_data = [
        (1, 'Mercedes-Benz', 'Sprinter', '2025-01-01 00:00:00'),
    ]
    
    cursor.executemany('INSERT INTO campers VALUES (?, ?, ?, ?)', sample_data)
    return cursor

def test_get_campers_data(create_db):
    cursor = create_db
    data = get_campers_data(cursor)
    # -s
    print(data)
    assert data[0] == {'marka': 'Mercedes-Benz', 'model': 'Sprinter'}
