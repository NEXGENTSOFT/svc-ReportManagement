import pika
import json

class RabbitMQService:
    def __init__(self, rabbitmq_url):
        self.rabbitmq_url = rabbitmq_url
        self.connection = None

    async def connect(self):
        self.connection = await pika.AsyncioConnection(pika.ConnectionParameters(host=self.rabbitmq_url))

    async def publish_message(self, exchange, routing_key, message):
        if not self.connection:
            raise Exception('Conexión RabbitMQ no establecida')

        channel = await self.connection.channel()
        await channel.exchange_declare(exchange=exchange, exchange_type='direct', durable=False)
        await channel.basic_publish(exchange=exchange, routing_key=routing_key, body=json.dumps(message))
        print(f"Mensaje publicado para intercambiar '{exchange}' con clave de enrutamiento '{routing_key}'")
