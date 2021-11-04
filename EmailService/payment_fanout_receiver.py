import pika
from EmailService import *

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='fanout2', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='fanout2', queue=queue_name)

def callback(ch, method, properties, body):
    bodysplit = body.split(";")
    order_id = bodysplit[0]
    payment_result=bodysplit[1]
    email_service = EmailService()
    EmailService().payment_email(order_id, payment_result)



channel.basic_consume(
    queue=queue_name, on_message_callback=callback(), auto_ack=True)

channel.start_consuming()
