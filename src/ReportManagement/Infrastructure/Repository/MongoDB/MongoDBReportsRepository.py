from bson import ObjectId
from src.ReportManagement.Domain.Ports.ReportsPort import ReportsPort
from src.ReportManagement.Domain.Entity.Reports import Report
from src.ReportManagement.Infrastructure.Models.MongoDB.MongoDBReportsModel import ReportsModel
from src.Database.MongoDB.connection import reports_collection
from loguru import logger

class ReportesRepository(ReportsPort):
    def __init__(self):
        self.collection = reports_collection

    def get_report(self):
        repor = list(self.collection.find({}, {"_id": 0}))
        status = True if repor else False
        message = "Reporte(s) encontrados exitosamente" if status else "Reporte(s) no encontrados"
        status_code = 200 if status else 500
        return {
            "data": repor,
            "message": message,
            "status": status
        }, status_code

    def create_report(self, reports: list[dict]):
        for report in reports:
            if 'id' in report and isinstance(report['id'], str):
                report['_id'] = ObjectId(report.pop('id'))
        result = self.collection.insert_many(reports)
        if result.inserted_ids:
            return {
                "data": reports,
                "message": "Reporte(s) creados exitosamente",
            }, 201
        else:
            return {
                "data": [],
                "message": "Error al crear reportes",
                "status": False
            }, 500

    def delete_report(self, id: str):
        try:
            result = self.collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count > 0:
                return {
                    "message": "Reporte eliminado con éxito",
                    "status": True
                }, 200
            else:
                return {
                    "message": "Reporte no encontrado",
                    "status": False
                }, 404
        except Exception as e:
            return {
                "message": str(e),
                "status": False
            }, 500

    def update_report(self, report_id: str = None, title: str = None, update_data: dict = {}):
        try:
            if report_id:
                reso = self.collection.find_one({"_id": ObjectId(report_id)})
            elif title:
                reso = self.collection.find_one({"title": title})
            else:
                return {
                    "data": {},
                    "message": "ID o título requerido",
                    "status": False
                }, 400

            if not reso:
                return {
                    "data": {},
                    "message": "Reporte no encontrado",
                    "status": False
                }, 404

            result = self.collection.update_one({"_id": ObjectId(reso["_id"])}, {"$set": update_data})
            if result.modified_count > 0:
                updated_repo = self.collection.find_one({"_id": ObjectId(reso["_id"])}, {"_id": 0})
                return {
                    "data": updated_repo,
                    "message": "Actualización exitosa",
                    "status": True
                }, 200
            else:
                return {
                    "data": {},
                    "message": "Error al actualizar",
                    "status": False
                }, 500
        except Exception as e:
            return {
                "data": {},
                "message": str(e),
                "status": False
            }, 500
