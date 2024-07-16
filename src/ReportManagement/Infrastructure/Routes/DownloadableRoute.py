from bson import ObjectId
from flask import Flask, request, Blueprint, jsonify
from src.ReportManagement.Infrastructure.Controllers.DownloadableControllers.CreateDownloadableController import CreateDownloadableController
from src.ReportManagement.Infrastructure.Controllers.DownloadableControllers.GetDownloadableController import GetDownloadableController
from src.ReportManagement.Infrastructure.Controllers.DownloadableControllers.UpdateDownloadableController import UpdateDownloadableController
from src.ReportManagement.Infrastructure.Controllers.DownloadableControllers.DeleteDownloadableController import DeleteDownloadableController
from src.ReportManagement.Infrastructure.Repository.MongoDB.MongoDBDownloadableRepository import DownloadableRepository


downloadable_routes = Blueprint('downloadable_routes', __name__)


dow = DownloadableRepository()
get_controller = GetDownloadableController(dow)
delete_controller = DeleteDownloadableController(dow)
create_controller = CreateDownloadableController(dow)
update_controller = UpdateDownloadableController(dow)

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
            channel.queue_declare(queue='queue.change_downloadable', durable=True)
            channel.basic_consume(queue='queue.change_downloadable', on_message_callback=callback)
            channel.start_consuming()
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error connecting to RabbitMQ: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    thread = Thread(target=consume)
    thread.start()
'''


@downloadable_routes.route("/downloadable", methods=["POST"])
def create_downloadable():
    data = request.get_json()
    if isinstance(data, list) and all(isinstance(item, dict) for item in data):
        return create_controller.run(data)
    else:
        return jsonify({"error": "Invalid data format"}), 400

@downloadable_routes.route("/downloadable/<string:id>", methods=["DELETE"])
def delete_downloadable(id):
    return delete_controller.run(id)

@downloadable_routes.route("/downloadable/<string:id_or_title>", methods=["PUT"])
def update_downloadable(id_or_title):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No update data provided"}), 400

    if ObjectId.is_valid(id_or_title):
        return update_controller.run(id=id_or_title, payload=data)
    else:
        return update_controller.run(title=id_or_title, payload=data)

@downloadable_routes.route("/downloadable", methods=["GET"])
def get_downloadable():
    report_type = request.args.get('report_type')
    report_data = request.args.to_dict()
    return get_controller.run(report_type, report_data)
