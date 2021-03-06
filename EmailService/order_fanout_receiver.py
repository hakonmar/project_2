import pika
from EmailService import *

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='fanout1', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='fanout1', queue=queue_name)

def callback(ch, method, properties, body):
    bodysplit = body.split(";")
    order_id = bodysplit[0]
    prod_name = bodysplit[9]
    total_price = bodysplit[10]
    buyer_email = bodysplit[11]
    merchant_email = bodysplit[12]
    email_service = EmailService()
    email_service.order_created_email(order_id, prod_name, total_price, buyer_email, merchant_email)




channel.basic_consume(
    queue=queue_name, on_message_callback=callback(), auto_ack=True)

channel.start_consuming()

