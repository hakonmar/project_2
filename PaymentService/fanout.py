import pika
import sys
import uuid

class fanout():
    def __init__(self):
        self.connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))

        self.channel = connection.channel()
        self.channel.exchange_declare(exchange='fanout2', exchange_type='fanout')



    def call(self, string:str, key:str):
        self.channel.basic_publish(exchange='fanout2', routing_key=key, body=string)
        print(" [x] Sent %r" % string)
        self.connection.close()