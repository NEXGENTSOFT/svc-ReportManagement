from bson import ObjectId
from src.ReportManagement.Domain.Ports.ReportsPort import ReportsPort
from src.ReportManagement.Domain.Entity.Reports import Report
from src.ReportManagement.Infrastructure.Models.MongoDB.MongoDBReportsModel import ReportsModel

class ReportesRepository(ReportsPort):
    def __init__(self):
        self.collection = ReportsModel.get_collection()

    def get_report(self):
        reports = list(self.collection.find({}, {"id": 0}))
        status = True if reports else False
        message = "Reportes encontrados exitosamente" if status else "Reportes no encontrados"
        status_code = 200 if status else 500
        return {
            "data": reports,
            "message": message,
            "status": status
        }, status_code

    def create_report(self, report: list[Report]):
        result = self.collection.insert_many(report)
        if result.inserted_ids:
            return {
                "data": report,
                "message": "Reportes creados exitosamente",
            }, 201
        else:
            return {
                "data": [],
                "message": "Error al crear reportes",
                "status": False
            }, 500

    def delete_report(self, id: str):
        result = self.collection.delete_one({"id": ObjectId(id)})
        status_code = 200
        if result.deleted_count == 0:
            return {
                "message": "Reporte no encontrado",
                "status": False
            }, 500
        else:
            return {
                "message": "Reporte eliminado con éxito",
                "status": True
            }, status_code

    def update_report(self, id: str = None, title: str = None, new_quantity: int = 0):
        if id:
            reporte = self.collection.find_one({"id": ObjectId(id)})
        elif title:
            reporte = self.collection.find_one({"title": title})
        else:
            return {
                "data": {},
                "message": "ID o título requerido",
                "status": False
            }, 400

        if not reporte:
            return {
                "data": {},
                "message": "Reporte no encontrado",
                "status": False
            }, 500

        result = self.collection.update_one({"id": ObjectId(reporte["id"])}, {"$set": {"stock": new_quantity}})
        if result.modified_count > 0:
            updated_reporte = self.collection.find_one({"id": ObjectId(reporte["id"])}, {"id": 0})
            return {
                "data": updated_reporte,
                "message": "Actualizada con éxito",
                "status": True
            }, 200
        else:
            return {
                "data": {},
                "message": "Error al actualizar",
                "status": False
            }, 500
