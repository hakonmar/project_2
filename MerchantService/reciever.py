import pika
from MerchantService import MerchantService



class reciever():
    def __init__(self) -> None:
        self.merchant = MerchantService
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = connection.channel()

        self.channel.queue_declare(queue='rpc_queue_merch_check')

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue='rpc_queue_merch_check', on_message_callback=self.recieve())

        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()


    def recieve(self, ch, method, props, body):
        id = int(body)
        response = self.merchant.check_id(id)

        ch.basic_publish(exchange='',
                        routing_key=props.reply_to,
                        properties=pika.BasicProperties(correlation_id = \
                                                            props.correlation_id),
                        body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)