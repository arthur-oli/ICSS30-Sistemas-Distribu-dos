import pika
import sys

possible_topics = {"cinema", "esportes", "saude", "politica", "broadcast"}
routing_key = sys.argv[1] if len(sys.argv) > 2 else "broadcast"
if (routing_key not in possible_topics):
    print(f"Topic must be one of these: {', '.join(possible_topics)}")
    sys.exit(1)

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="newsletterTopic", exchange_type="topic")

message = " ".join(sys.argv[2:]) or "Standard message"
channel.basic_publish(exchange="newsletterTopic", routing_key=routing_key, body=message)
print(f"[x] Sent on topic {routing_key}: {message}")
connection.close()