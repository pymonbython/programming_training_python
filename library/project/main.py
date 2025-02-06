from datetime import datetime
from string import Template
from os import getenv
import sqlite3
import email

from dotenv import load_dotenv

from lenders import get_lenders_by_return_date
from emails import EmailSender, Credentials
from  db import Database

load_dotenv()

CONNECTION = sqlite3.connect(getenv('DB_NAME'))

ssl_enable = getenv('SSL_ENABLE', False)
port = getenv('PORT')
smtp_server = getenv('SMTP_SERVER')
username = getenv('MAIL_USERNAME')
password = getenv('MAIL_PASSWORD')
subject = getenv('SUBJECT')
sender =  getenv('SENDER')

def setup(connection):
    with Database(connection) as database:
        database.cursor.execute('''CREATE TABLE lender(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            car_model TEXT,
            car_return_at DATE
            email TEXT)''')

def send_reminder_to_lender(lender):
        template = Template('''Panie $name!
                    
        Wypożyczyłeś $car_model.
        Prosimy o natychmiastowy zwrot wynajętego auta, najpóźniej do dnia $car_return_at.

        Z poważaniem
                            
        Agnieszka Kowalczyk z firmy Rent Four Wheels.''')
        receiver_template = Template('Receiver <$lender_email>')
        text = template.substitute({
            'name': lender.name,
            'car_model': lender.car_model,
            'car_return_at': lender.car_return_at
        })
        receiver = receiver_template.substitute({
            'lender_email': lender.email
        })
        message = email.message_from_string(text)
        message.set_charset('utf-8')
        message['from'] = sender
        message['to'] = receiver
        message['Subject'] = subject
        email_sender.sendmail(sender, receiver, message)

        print(f'Wysyłam e-mail do {lender.email}...')

if __name__ == '__main__':
    today_date = datetime.today().strftime('%Y-%m-%d')
    lenders = get_lenders_by_return_date(CONNECTION, today_date)

    with EmailSender(port, smtp_server, Credentials(username, password)) as email_sender:
        for lender in lenders:
            send_reminder_to_lender(lender)
            print('Success.')
