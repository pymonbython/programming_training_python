from datetime import datetime
from string import Template
import sqlite3
import email

from lenders import get_lenders_by_return_date
from emails import EmailSender, Credentials
from  db import Database


ssl_enable = False
port = 2525
smtp_server = 'sandbox.smtp.mailtrap.io'
username = 'efd24571950570'
password = 'da9a0378cd0db2'
subject = 'Przypomnienie o obowiązkowym zwrocie wynajętego pojazdu.'
sender = 'Sender <sender@gmail.com>'
receiver_template = Template('Receiver <$lender_email>')

CONNECTION = sqlite3.connect('database.db')

def setup(connection):
    with Database(connection) as database:
        database.cursor.execute('''CREATE TABLE lender(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            car_model TEXT,
            car_return_at DATE
            email TEXT)''')

today_date = datetime.today().strftime('%Y-%m-%d')

lenders = get_lenders_by_return_date(CONNECTION, today_date)
print(lenders)

template = Template('''Panie $name!
                    
Wypożyczyłeś $car_model.
Prosimy o natychmiastowy zwrot wynajętego auta, najpóźniej do dnia $car_return_at.

Z poważaniem
                    
Agnieszka Kowalczyk z firmy Rent Four Wheels.''')

with EmailSender(port, smtp_server, Credentials(username, password)) as email_sender:
    for lender in lenders:
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
    
    print('Success.')
