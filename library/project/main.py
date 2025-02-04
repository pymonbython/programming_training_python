from datetime import datetime
import sqlite3
import smtplib
import email
import ssl

from lenders import get_lenders_by_return_date
from  db import Database


CONNECTION = sqlite3.connect('database.db')

def setup(connection):
    with Database(connection) as database:
        database.cursor.execute('''
        CREATE TABLE lender(
            id integer primary key autoincrement,
            name text,
            car_model text,
            car_return_at date)
        ''')

# print(datetime.today().strftime('%Y-%m-%d'))

# lenders = get_lenders_by_return_date(CONNECTION, '2025-02-01)')
# print(lenders)

ssl_enable = False
port = 2525
smtp_server = 'sandbox.smtp.mailtrap.io'
username = 'efd24571950570'
password = 'da9a0378cd0db2'
subject = 'Oddawaj książkę!'
sender = 'Sender <sender@gmail.com>'
receiver = 'Receiver <receiver@gmail.com>'

messeage = email.message_from_string(f'''
    Subject: {subject}
    To: {receiver}
    From: {sender}

    Oddaj mi książkę!
''')
messeage.set_charset('utf-8')

if not ssl_enable:
    connection = smtplib.SMTP(smtp_server, port)

else:
    context = ssl.create_default_context()
    connection = smtplib.SMTP_SSL(smtp_server, port, context)

connection.login(username, password)
connection.sendmail(sender, receiver, messeage.as_string())
connection.quit()
