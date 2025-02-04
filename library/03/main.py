import smtplib, ssl
from collections import namedtuple

def send_mail():
    context = ssl.create_default_context()
    smtp_server = "smtp.gmail.com"
    port = 465
    sender_email = ''
    password = ''

    with smtplib.SMTP_SSL(smtp_server, port=port, context=context) as server:
        server.login(sender_email, password=password)
        server.sendmail(sender_email, sender_email, 'Honda is the best!')

class User:
    def __init__(self, username, lastname):
        self.username = username
        self.lastname = lastname

user1 = User('test', 'test')
print(user1)


tuple1 = ('name', 'surname')
print(tuple1)

User = namedtuple('User', 'name lastname')

