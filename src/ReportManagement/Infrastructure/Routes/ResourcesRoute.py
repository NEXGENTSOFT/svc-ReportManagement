from bson import ObjectId
from flask import Flask, request, Blueprint, jsonify
from src.ReportManagement.Infrastructure.Controllers.ResourcesControllers.CreateResourcesController import CreateResourcesController
from src.ReportManagement.Infrastructure.Controllers.ResourcesControllers.UpdateResourcesController import UpdateResourcesController
from src.ReportManagement.Infrastructure.Controllers.ResourcesControllers.DeleteResourcesController import DeleteResourcesController
from src.ReportManagement.Infrastructure.Controllers.ResourcesControllers.GetResourcesController import GetResourcesController
from src.ReportManagement.Infrastructure.Repository.MongoDB.MongoDBResourcesRepository import ResourcesRepository



resources_routes = Blueprint('resources_routes', __name__)

reso = ResourcesRepository()
get_controller = GetResourcesController(reso)
delete_controller = DeleteResourcesController(reso)
create_controller = CreateResourcesController(reso)
update_controller = UpdateResourcesController(reso)

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
            channel.queue_declare(queue='queue.change_resources', durable=True)
            channel.basic_consume(queue='queue.change_resources', on_message_callback=callback)
            channel.start_consuming()
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error connecting to RabbitMQ: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    thread = Thread(target=consume)
    thread.start()
'''


@resources_routes.route("/resource", methods=["GET"])
def get_resources():
    return get_controller.run()

@resources_routes.route("/resource", methods=["POST"])
def create_resources():
    data = request.get_json()
    if isinstance(data, list) and all(isinstance(item, dict) for item in data):
        return create_controller.run(data)
    else:
        return jsonify({"error": "Invalid data format"}), 400

@resources_routes.route("/resource/<string:id>", methods=["DELETE"])
def delete_resources(id):
    return delete_controller.run(id)
@resources_routes.route("/resource/<string:id_or_title>", methods=["PUT"])
def update_resources(id_or_title):
    if ObjectId.is_valid(id_or_title):
        return update_controller.run(id_or_title)
    else:
        return update_controller.run(title=id_or_title)

