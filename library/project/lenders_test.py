import sqlite3

import pytest

from lenders import get_lenders_by_return_date


@pytest.fixture
def create_connection():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE lender(
            id integer primary key autoincrement,
            name text,
            car_model text,
            car_return_at date)
        ''')
    
    sample_data = [
        (1, 'Borrower1', 'Sprinter 903', '2024-02-01'),
        (2, 'Borrower2', 'Viano 2008', '2025-03-03')
    ]

    cursor.executemany('''
        INSERT INTO lender VALUES(?, ?, ?, ?)
    ''', sample_data)

    return connection


def test_get_lenders_by_return_date(create_connection):
    lenders = get_lenders_by_return_date(create_connection, '2025-03-01')
    print(lenders)

    assert lenders[0].name == 'Borrower1'
