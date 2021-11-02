import yagmail
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv(Email)
email_password = os.getenv(Email_Password)

yag = yagmail.SMTP(email, email_password)

contents = []

yag.send("receiver", "subject", contents)
