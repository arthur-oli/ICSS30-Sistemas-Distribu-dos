import pika
import sys

possible_topics = {"cinema", "esportes", "saude", "politica"}

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="newsletterTopic", exchange_type="topic")
channel.exchange_declare(exchange="newsletterBroadcast", exchange_type="fanout")

result = channel.queue_declare("", exclusive=True)
queue_name = result.method.queue

binding_keys = input("[x] Which topics to subscribe to? Separate with spaces.\n")

for binding_key in binding_keys.split(" "):
    if binding_key not in possible_topics:
        print(f"[x] Topic must be one of these: {', '.join(possible_topics)}")
        sys.exit(1)
    channel.queue_bind(exchange="newsletterTopic", queue=queue_name, routing_key=binding_key)

channel.queue_bind(exchange="newsletterBroadcast", queue=queue_name)

print("[x] Waiting for logs. To exit press CTRL+C.")

def callback(ch, method, properties, body):
    if method.routing_key == "broadcast":
        print(f"[x] Received on broadcast: {body.decode()}")
    else:
        print(f"[x] Received on topic {method.routing_key}: {body.decode()}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()