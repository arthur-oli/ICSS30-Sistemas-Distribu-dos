import pika

a = input("Digite sua mensagem: ")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=a)
print(f" [x] Sent message '{a}'")
connection.close()