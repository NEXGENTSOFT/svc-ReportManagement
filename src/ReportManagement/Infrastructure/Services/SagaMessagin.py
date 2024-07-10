import uuid

from flask import Flask, request, jsonify
import pika
import json
import asyncio

app = Flask(__name__)


async def send_message_and_wait_for_response(event, data):
    connection = await pika.AsyncioConnection(pika.ConnectionParameters(host='localhost'))
    channel = await connection.channel()

    exchange = 'saga_exchange'
    await channel.exchange_declare(exchange=exchange, exchange_type='direct', durable=False)

    response_queue = await channel.queue_declare(queue='', exclusive=True)
    callback_queue = response_queue.method.queue

    correlation_id = generate_correlation_id()

    response_promise = asyncio.Future()

    def on_response(ch, method, properties, body):
        if properties.correlation_id == correlation_id:
            response = json.loads(body.decode())
            response_promise.set_result(response)
            ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=callback_queue, on_message_callback=on_response, auto_ack=True)

    await channel.basic_publish(
        exchange=exchange,
        routing_key=event,
        body=json.dumps(data),
        properties=pika.BasicProperties(
            reply_to=callback_queue,
            correlation_id=correlation_id
        )
    )

    print(f"[x] Sent {event}: {data}")

    return await response_promise


def generate_correlation_id():
    return str(uuid.uuid4())


# Ruta en Flask para manejar la solicitud y enviarla a RabbitMQ
@app.route('/send_and_receive', methods=['POST'])
def send_and_receive():
    request_data = request.json
    event = request_data['event']
    data = request_data['data']

    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(send_message_and_wait_for_response(event, data))
        loop.close()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

