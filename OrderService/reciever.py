import pika
from OrderService import OrderService



def recieve(ch, method, props, body):
    request = get_dict(body)
    response = order.place_order(request)

    ch.basic_publish(exchange='',
                    routing_key=props.reply_to,
                    properties=pika.BasicProperties(correlation_id = \
                                                        props.correlation_id),
                    body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

def get_dict(body):
    body_split = body.split(';')
    request_dict = dict()
    request_dict["productId"] = body_split[0]
    request_dict["merchantId"] = body_split[1]
    request_dict["buyerId"] = body_split[2]
    request_dict["creditCard"] = dict()
    request_dict["credidCard"]["cardNumber"] = body_split[3]
    request_dict["credidCard"]["expirationMonth"] = body_split[4]
    request_dict["credidCard"]["expirationYear"] = body_split[5]
    request_dict["credidCard"]["cvc"] = body_split[6]
    request_dict["discount"] = body_split[7]
    return request_dict



order = OrderService()
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue_post_order')

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue_post_order', on_message_callback=recieve())

# print(" [x] Awaiting RPC requests")
channel.start_consuming()
