import smtplib
import ssl
from os import getenv
"""
This is a script that send emails.
"""

email = "test"


def send_email(extrac):
    """Send an email when there is upcoming tour"""
    host = "smtp.gmail.com"
    port = 465

    username = email
    password = getenv("PASSWORD")

    receiver = email
    context = ssl.create_default_context()
    message = ""
    message = "Subject: Hey, new event was found!" + '\n' + \
              message + f"{extrac}"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message.encode("utf-8"))
    print("Email was sent!")