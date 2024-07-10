from bson import ObjectId
from flask import Flask, request, Blueprint
from src.ReportManagement.Infrastructure.Controllers.ResourcesControllers.CreateResourcesController import CreateResourcesController
from src.ReportManagement.Infrastructure.Controllers.ResourcesControllers.UpdateResourcesController import UpdateResourcesController
from src.ReportManagement.Infrastructure.Controllers.ResourcesControllers.DeleteResourcesController import DeleteResourcesController
from src.ReportManagement.Infrastructure.Controllers.ResourcesControllers.GetResourcesController import GetResourcesController
from src.ReportManagement.Infrastructure.Repository.MongoDB.MongoDBResourcesRepository import ResourcesRepository
import pika
import json
from threading import Thread


resource_routes = Blueprint('resources_routes', __name__)

app = Flask(__name__)

reso = ResourcesRepository()
get_controller = GetResourcesController(reso)
delete_controller = DeleteResourcesController(reso)
create_controller = CreateResourcesController(reso)
update_controller = UpdateResourcesController(reso)


def callback(ch, method, properties, body):
    update_controller.run(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_resources():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='queue.change_resources', durable=True)
    channel.basic_consume(queue='queue.change_resources', on_message_callback=callback)
    channel.start_consuming()


@app.route("/resources", methods=["GET"])
def get_resources():
    return get_controller.run()

@app.route("/resources", methods=["POST"])
def create_resources():
    return create_controller.run(request)

@app.route("/resources/<string:id>", methods=["DELETE"])
def delete_resources(id):
    return delete_controller.run(id)
@app.route("/resoucer/<string:id_or_title>", methods=["PUT"])
def update_resources(id_or_title):
    if ObjectId.is_valid(id_or_title):
        return update_controller.run(id_or_title)
    else:
        return update_controller.run(title=id_or_title)

