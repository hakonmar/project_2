import pika
from PaymentService import *
from fanout import *

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
    credit_card_info = []
    credit_card_info[0] = bodysplit[4]
    credit_card_info[1] = bodysplit[5]
    credit_card_info[2] = bodysplit[6]
    credit_card_info[3] = bodysplit[7]
    fanout = fanout()
    credit_card_info = credit_card_info.join(";")
    payment_result = payment_check(credit_card_info)
    bodysplit.append(str(payment_result))
    string = []
    string = bodysplit [0:1]
    string.append(bodysplit[11])
    string.append(bodysplit[12])
    string.append(str(payment_result))
    string.join(";")
    fanout.call(string)





channel.basic_consume(
    queue=queue_name, on_message_callback=callback(), auto_ack=True)

channel.start_consuming()

