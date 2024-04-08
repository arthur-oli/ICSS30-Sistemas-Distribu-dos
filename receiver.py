import pika
import sys

possible_topics = {"cinema", "esportes", "saude", "politica"}

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="newsletterTopic", exchange_type="topic")

result = channel.queue_declare("", exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    if binding_key not in possible_topics:
        print(f"Topic must be one of these: {', '.join(possible_topics)}")
        sys.exit(1)
    channel.queue_bind(exchange="newsletterTopic", queue=queue_name, routing_key=binding_key)

print("[*] Waiting for logs. To exit press CTRL+C")

def callback(ch, method, properties, body):
    print(f"[x] Received on topic {method.routing_key}: {body.decode()}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()