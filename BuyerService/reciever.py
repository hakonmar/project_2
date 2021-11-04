import pika
from BuyerService import BuyerService



def recieve(ch, method, props, body):
    id = int(body)
    response = buyer.check_id(id)

    ch.basic_publish(exchange='',
                    routing_key=props.reply_to,
                    properties=pika.BasicProperties(correlation_id = \
                                                        props.correlation_id),
                    body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

def recieve2(ch, method, props, body):
    id = int(body)
    response = buyer.get_buyer_info(id)

    ch.basic_publish(exchange='',
                    routing_key=props.reply_to,
                    properties=pika.BasicProperties(correlation_id = \
                                                        props.correlation_id),
                    body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


buyer = BuyerService()
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel2 = connection.channel()

channel.queue_declare(queue='rpc_queue_merch_check')

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue_merch_check', on_message_callback=recieve())

# print(" [x] Awaiting RPC requests")
channel.start_consuming()

channel2.queue_declare(queue='rpc_queue_email_merch')

channel2.basic_qos(prefetch_count=1)
channel2.basic_consume(queue='rpc_queue_email_merch', on_message_callback=recieve2())

channel2.start_consuming()