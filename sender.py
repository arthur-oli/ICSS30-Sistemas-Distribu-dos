import pika
import sys

possible_topics = {"cinema", "esportes", "saude", "politica", "broadcast"}
routing_key = input("[x] Which topic to publish to?\n")
if (routing_key not in possible_topics):
    print(f"[x] Topic must be one of these: {', '.join(possible_topics)}")
    sys.exit(1)

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
message = input(f"[x] Which message to send on topic {routing_key}?\n")

if(routing_key == "broadcast"):
    channel.exchange_declare(exchange="newsletterBroadcast", exchange_type="fanout")
    channel.basic_publish(exchange="newsletterBroadcast", routing_key="broadcast", body=message)
    print(f"[x] Sent on broadcast: {message}")

else:
    channel.exchange_declare(exchange="newsletterTopic", exchange_type="topic")
    channel.basic_publish(exchange="newsletterTopic", routing_key=routing_key, body=message)
    print(f"[x] Sent on topic {routing_key}: {message}")

connection.close()