from _typeshed import SupportsLenAndGetItem
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

def recieve3(ch, method, props, body):
    merch_n_prod_id = body.split(';')
    response = inventory.check_merchant(int(merch_n_prod_id[0]), int(merch_n_prod_id[1]))

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
channel3 = connection.channel()

channel.queue_declare(queue='rpc_queue_product_check')

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue_product_check', on_message_callback=recieve())

# print(" [x] Awaiting RPC requests")
channel.start_consuming()

channel2.queue_declare(queue='rpc_queue_product_check')

channel2.basic_qos(prefetch_count=1)
channel2.basic_consume(queue='rpc_queue_product_check', on_message_callback=recieve2())

channel2.start_consuming()

channel3.queue_declare(queue='rpc_queue_product_check')

channel3.basic_qos(prefetch_count=1)
channel3.basic_consume(queue='rpc_queue_product_check', on_message_callback=recieve3())

channel3.start_consuming()