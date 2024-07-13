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
        try:
            reports = list(self.collection.find({}, {"id": 0}))
            logger.info(f"Reports fetched: {reports}")
            status = True if reports else False
            message = "Reportes encontrados exitosamente" if status else "Reportes no encontrados"
            status_code = 200 if status else 500
            return {
                "data": reports,
                "message": message,
                "status": status
            }, status_code
        except Exception as e:
            logger.error(f"Failed to get reports: {e}")
            return {
                "data": [],
                "message": "Error al obtener reportes",
                "status": False
            }, 500

    def create_report(self, report: list[Report]):
        try:
            result = self.collection.insert_many(report)
            logger.info(f"Reports inserted: {result.inserted_ids}")
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
        except Exception as e:
            logger.error(f"Failed to create reports: {e}")
            return {
                "data": [],
                "message": "Error al crear reportes",
                "status": False
            }, 500

    def delete_report(self, id: str):
        try:
            result = self.collection.delete_one({"id": ObjectId(id)})
            logger.info(f"Reports deleted count: {result.deleted_count}")
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
        except Exception as e:
            logger.error(f"Failed to delete report: {e}")
            return {
                "message": "Error al eliminar reporte",
                "status": False
            }, 500

    def update_report(self, id: str = None, title: str = None, new_quantity: int = 0):
        try:
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
            logger.info(f"Reports updated count: {result.modified_count}")
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
        except Exception as e:
            logger.error(f"Failed to update report: {e}")
            return {
                "data": {},
                "message": "Error al actualizar reporte",
                "status": False
            }, 500
