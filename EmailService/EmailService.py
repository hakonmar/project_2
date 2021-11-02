import yagmail
from dotenv import load_dotenv
import os



class EmailService():
    def __init__(self) -> None:
        load_dotenv()

        email = os.getenv(Email)
        email_password = os.getenv(Email_Password)

        self.yag = yagmail.SMTP(email, email_password)


    def send_email(self, reciever:str, subject, contents):
        self.yag.send(reciever, subject, contents)
