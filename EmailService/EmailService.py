import yagmail
from dotenv import load_dotenv
import os
import pika


class EmailService():
    def __init__(self) -> None:
        load_dotenv()

        email = os.getenv(Email)
        email_password = os.getenv(Email_Password)

        self.yag = yagmail.SMTP(email, email_password)

    def send_email(self, reciever:str, subject, contents):
        self.yag.send(reciever, subject, contents)

    def order_created_email(self, order_id, prod_name, total_price, buyer, merchant):
        self.send_email(buyer, "Order has been created", f"Order ID: {order_id}\nProduct name: {prod_name}\nTotal: {total_price}")
        self.send_email(merchant, "Order has been created", f"Order ID: {order_id}\nProduct name: {prod_name}\nTotal: {total_price}")
    
    def payment_email(self, order_id, result, buyer, merchant):
        if result==1:
            self.send_email(buyer, "Order has been purchased", f"Order {order_id} has been successfully purchased")
            self.send_email(merchant, "Order has been purchased", f"Order {order_id} has been successfully purchased")

        else:
            self.send_email(buyer, "Order purchase failed",  f"Order {order_id} purchase has failed")
            self.send_email(merchant, "Order purchase failed",  f"Order {order_id} purchase has failed")