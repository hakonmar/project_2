import pika
from InventoryService import *

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='fanout2', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='fanout2', queue=queue_name)

def callback(ch, method, properties, body):
    bodysplit = body.split(";")
    payment_service = InventoryService()()
    order_id = bodysplit[0]
    prod_id=bodysplit[1]
    payment_result=bodysplit[4]
    if payment_result==1:
        payment_service.product_bought(prod_id)




channel.basic_consume(
    queue=queue_name, on_message_callback=callback(), auto_ack=True)

channel.start_consuming()

