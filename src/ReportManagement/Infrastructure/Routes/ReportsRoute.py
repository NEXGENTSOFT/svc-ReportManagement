from bson import ObjectId
from flask import Flask, request, Blueprint
from src.ReportManagement.Infrastructure.Controllers.ReportsControllers.CreateReportsController import CreateReportsController
from src.ReportManagement.Infrastructure.Controllers.ReportsControllers.UpdateReportsController import UpdateReportsController
from src.ReportManagement.Infrastructure.Controllers.ReportsControllers.DeleteReportsController import DeleteReportsController
from src.ReportManagement.Infrastructure.Controllers.ReportsControllers.GetReportsController import GetReportsController
from src.ReportManagement.Infrastructure.Repository.MongoDB.MongoDBReportsRepository import ReportesRepository
import pika
import json
from threading import Thread
report_routes = Blueprint('report_routes', __name__)

app = Flask(__name__)

repo = ReportesRepository()
get_controller = GetReportsController(repo)
delete_controller = DeleteReportsController(repo)
create_controller = CreateReportsController(repo)
update_controller = UpdateReportsController(repo)


def callback(ch, method, properties, body):
    update_controller.run(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_report():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='queue.change_report', durable=True)
    channel.basic_consume(queue='queue.change_report', on_message_callback=callback)
    channel.start_consuming()


@app.route("/reports", methods=["GET"])
def get_report():
    return get_controller.run()

@app.route("/reports", methods=["POST"])
def create_report():
    return create_controller.run(request)

@app.route("/reports/<string:id>", methods=["DELETE"])
def delete_report(id):
    return delete_controller.run(id)
@app.route("/reports/<string:id_or_title>", methods=["PUT"])
def update_report(id_or_title):
    if ObjectId.is_valid(id_or_title):
        return update_controller.run(id_or_title)
    else:
        return update_controller.run(title=id_or_title)

