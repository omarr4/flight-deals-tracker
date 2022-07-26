import smtplib
from email.message import EmailMessage
import os


class NotificationManager:
    def __init__(self, to_email):
        self.from_email = "exampleemail@gmail.com"
        self.e_password = "example password"
        self.to_email = to_email
        self.subject = "Flight Deals"

    def send_email(self, msg):
        message = EmailMessage()
        message.add_header("From", self.from_email)
        message.add_header("To", self.to_email)
        message.add_header("Subject", self.subject)
        message.set_payload(msg, "utf-8")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.from_email, password=self.e_password)
            connection.send_message(message, from_addr=self.from_email, to_addrs=self.to_email)
