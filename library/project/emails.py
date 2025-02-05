from collections import namedtuple
import smtplib
import ssl


Credentials = namedtuple('Credentials', 'username password')


class EmailSender:
    def __init__(self, port: int, smtp_address: str, credentials: tuple, ssl_enabled=False) -> None:
        self.port = port
        self.smtp_address = smtp_address
        self.credentials = credentials
        self.ssl_enabled = ssl_enabled
        self.connection = None


    def __enter__(self):
        if not self.ssl_enabled:
            self.connection = smtplib.SMTP(self.smtp_address, self.port)

        else:
            context = ssl.create_default_context()
            self.connection = smtplib.SMTP_SSL(self.smtp_server, self.port, context)

        self.connection.login(self.credentials.username, self.credentials.password)

        return self

    
    def sendmail(self, sender: str, receiver:str, message) -> None:
        self.connection.sendmail(sender, receiver, message.as_string())

    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.connection.quit()
