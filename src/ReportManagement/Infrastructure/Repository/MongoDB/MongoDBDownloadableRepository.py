from bson import ObjectId
from src.ReportManagement.Domain.Ports.DownloadablePort import DownloadablePort
from src.ReportManagement.Domain.Entity.Downloadable import Downloadable
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from src.Database.MongoDB.connection import downloadable_collection
import os

class DownloadableRepository(DownloadablePort):
    def __init__(self):
        self.collection = downloadable_collection

    def get_downloadable(self, report_url: str, report_data: dict):
        if report_url == "1":
            report_content = f"Reporte 1 {report_data.get('date', 'No Date Provided')}"
        elif report_url == "2":
            report_content = f"Reporte 2 {report_data.get('date', 'No Date Provided')}"
        elif report_url == "3":
            report_content = f"Reporte 3 {report_data.get('date', 'No Date Provided')}"
        elif report_url == "4":
            report_content = f"Reporte 4 {report_data.get('date', 'No Date Provided')}"
        else:
            return {
                "data": {},
                "message": f"Tipo de reporte no soportado: {report_url}",
                "status": False
            }, 400

        # Generar PDF y guardar
        pdf_filename = f"reporte_{report_url}_{report_data.get('date', 'no_date')}.pdf"
        pdf_path = os.path.join("/ruta/donde/guardar", pdf_filename)  # Ajusta la ruta según tu entorno
        self.generate_pdf(pdf_path, report_content)

        return {
            "data": {"pdf_path": pdf_path},
            "message": "Reporte generado exitosamente",
            "status": True
        }, 200

    def generate_pdf(self, pdf_path: str, content: str):
        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.drawString(100, 750, content)
        c.save()

    def create_downloadable(self, downloadables: list[Downloadable]):
        # Convertir objetos Downloadable a diccionarios antes de insertarlos
        downloadable_dicts = [d.dict(by_alias=True) for d in downloadables]
        for item in downloadable_dicts:
            if 'id' in item and isinstance(item['id'], str):
                item['_id'] = ObjectId(item.pop('id'))
        result = self.collection.insert_many(downloadable_dicts)
        if result.inserted_ids:
            return {
                "data": downloadable_dicts,
                "message": "Descarga creada exitosamente",
            }, 201
        else:
            return {
                "data": [],
                "message": "Error al crear descarga",
                "status": False
            }, 500

    def delete_downloadable(self, id: str):
        try:
            result = self.collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count > 0:
                return {
                    "message": "Descarga eliminada con éxito",
                    "status": True
                }, 200
            else:
                return {
                    "message": "Descarga no encontrada",
                    "status": False
                }, 404
        except Exception as e:
            return {
                "message": str(e),
                "status": False
            }, 500

    def update_downloadable(self, id: str = None, title: str = None, update_data: dict = {}):
        try:
            if id:
                reso = self.collection.find_one({"_id": ObjectId(id)})
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
                    "message": "Descarga no encontrada",
                    "status": False
                }, 404

            result = self.collection.update_one({"_id": ObjectId(reso["_id"])}, {"$set": update_data})
            if result.modified_count > 0:
                updated_reso = self.collection.find_one({"_id": ObjectId(reso["_id"])}, {"_id": 0})
                return {
                    "data": updated_reso,
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
