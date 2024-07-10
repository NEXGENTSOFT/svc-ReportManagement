from bson import ObjectId
from flask import Flask, request, Blueprint
from src.ReportManagement.Infrastructure.Controllers.DownloadableControllers.CreateDownloadableController import CreateDownloadableController
from src.ReportManagement.Infrastructure.Controllers.DownloadableControllers.GetDownloadableController import GetDownloadableController
from src.ReportManagement.Infrastructure.Controllers.DownloadableControllers.UpdateDownloadableController import UpdateDownloadableController
from src.ReportManagement.Infrastructure.Controllers.DownloadableControllers.DeleteDownloadableController import DeleteDownloadableController
from src.ReportManagement.Infrastructure.Repository.MongoDB.MongoDBDownloadableRepository import DownloadableRepository
import pika
import json
from threading import Thread

downloadable_routes = Blueprint('downloadable_routes', __name__)

app = Flask(__name__)

dow = DownloadableRepository()
get_controller = GetDownloadableController(dow)
delete_controller = DeleteDownloadableController(dow)
create_controller = CreateDownloadableController(dow)
update_controller = UpdateDownloadableController(dow)

def callback(ch, method, properties, body):
    update_controller.run(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_downloadable():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='queue.change_downloadable', durable=True)
    channel.basic_consume(queue='queue.change_downloadable', on_message_callback=callback)
    channel.start_consuming()


@app.route("/downloadable", methods=["GET"])
def get_downloadable():
    return get_controller.run()

@app.route("/downloadable", methods=["POST"])
def create_downloadable():
    return create_controller.run(request)

@app.route("/downloadable/<string:id>", methods=["DELETE"])
def delete_downloadable(id):
    return delete_controller.run(id)
@app.route("/downloadable/<string:id_or_title>", methods=["PUT"])
def update_downloadable(id_or_title):
    if ObjectId.is_valid(id_or_title):
        return update_controller.run(id_or_title)
    else:
        return update_controller.run(title=id_or_title)

