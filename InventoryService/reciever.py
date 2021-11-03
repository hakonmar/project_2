import pika
from InventoryService import InventoryService



def recieve(ch, method, props, body):
    id = int(body)
    response = inventory.check_id(id)

    ch.basic_publish(exchange='',
                    routing_key=props.reply_to,
                    properties=pika.BasicProperties(correlation_id = \
                                                        props.correlation_id),
                    body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def recieve2(ch, method, props, body):
    id = int(body)
    response = inventory.check_id(id)

    ch.basic_publish(exchange='',
                    routing_key=props.reply_to,
                    properties=pika.BasicProperties(correlation_id = \
                                                        props.correlation_id),
                    body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)



inventory = InventoryService()
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel2 = connection.channel()

channel.queue_declare(queue='rpc_queue_product_check')

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue_product_check', on_message_callback=recieve())

# print(" [x] Awaiting RPC requests")
channel.start_consuming()

channel2.queue_declare(queue='rpc_queue_product_check')

channel2.basic_qos(prefetch_count=1)
channel2.basic_consume(queue='rpc_queue_product_check', on_message_callback=recieve())

channel2.start_consuming()