
from flask import request, Blueprint, jsonify
from bson import ObjectId
from src.ReportManagement.Infrastructure.Controllers.ReportsControllers.CreateReportsController import CreateReportsController
from src.ReportManagement.Infrastructure.Controllers.ReportsControllers.UpdateReportsController import UpdateReportsController
from src.ReportManagement.Infrastructure.Controllers.ReportsControllers.DeleteReportsController import DeleteReportsController
from src.ReportManagement.Infrastructure.Controllers.ReportsControllers.GetReportsController import GetReportsController
from src.ReportManagement.Infrastructure.Repository.MongoDB.MongoDBReportsRepository import ReportesRepository

report_routes = Blueprint('report_routes', __name__)

repo = ReportesRepository()
get_controller = GetReportsController(repo)
delete_controller = DeleteReportsController(repo)
create_controller = CreateReportsController(repo)
update_controller = UpdateReportsController(repo)
'''
def callback(ch, method, properties, body):
    update_controller.run(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_report():
    def consume():
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost',
                port=5672,
                virtual_host='/',
                credentials=pika.PlainCredentials('guest', 'guest')
            ))
            channel = connection.channel()
            channel.queue_declare(queue='queue.change_report', durable=True)
            channel.basic_consume(queue='queue.change_report', on_message_callback=callback)
            channel.start_consuming()
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error connecting to RabbitMQ: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    thread = Thread(target=consume)
    thread.start()
'''
@report_routes.route("/report", methods=["GET"])
def get_report():
    return get_controller.run()

@report_routes.route("/report", methods=["POST"])
def create_resources():
    data = request.get_json()  # Espera un diccionario o una lista de diccionarios
    if isinstance(data, list) and all(isinstance(item, dict) for item in data):
        return create_controller.run(data)
    else:
        return jsonify({"error": "Invalid data format"}), 400


@report_routes.route("/report/<string:id>", methods=["DELETE"])
def delete_report(id):
    return delete_controller.run(id)

@report_routes.route("/report/<string:id_or_title>", methods=["PUT"])
def update_report(id_or_title):
    if ObjectId.is_valid(id_or_title):
        return update_controller.run(id_or_title)
    else:
        return update_controller.run(title=id_or_title)
