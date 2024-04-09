# ICSS30-Sistemas-Distribuidos
Trabalhos da disciplina ICSS30.

Trabalho 1:
sender.py e receiver.py

Uma aplicação simples orientada a microsserviços. Em cada microsserviço devem ocorrer eventos que sejam de interesse de outros microsserviços. A comunicação entre os microsserviços é orientada a eventos.
- Dois ou mais clientes publicadores podem gerar eventos (mensagens); 
- Dois ou mais clientes consumidores ou assinantes podem registrar interesse em receber notificações de eventos;
- Utilizado o serviço de mensageria (message broker) RabbitMQ e o protocolo AMQP (Advanced Message Queuing Protocol) para permitir a comunicação indireta entre os processos clientes. O broker é responsável por enviar notificações de eventos aos clientes assinantes interessados.
