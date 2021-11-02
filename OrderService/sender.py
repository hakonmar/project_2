import pika
import sys
    

class sender():
    def __init__(self) -> None:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange='logs', exchange_type='fanout')

    def sender_check(self):
        pass