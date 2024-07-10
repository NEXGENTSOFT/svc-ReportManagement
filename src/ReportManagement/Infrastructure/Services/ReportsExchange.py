import pika

async def declare_report_exchange():
    try:
        connection = await pika.AsyncioConnection(pika.ConnectionParameters(host='localhost'))
        channel = await connection.channel()

        exchange_name = 'reports-exchange'
        exchange_type = 'direct'

        await channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type, durable=False)

        print("Exchange 'reports-exchange' declared successfully.")

    except Exception as error:
        print(f"ERROR: {error}")