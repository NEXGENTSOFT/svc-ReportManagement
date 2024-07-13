from bson import ObjectId
from src.ReportManagement.Domain.Ports.DownloadablePort import DownloadablePort
from src.ReportManagement.Domain.Entity.Downloadable import Downloadable
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from src.Database.MongoDB.connection import downloadable_collection
class DownloadableRepository(DownloadablePort):
    def __init__(self):
        self.collection = downloadable_collection
    def get_downloadable(self, report_type: str, report_data: dict):
        if report_type == "1":
            report_content = f"Reporte 1 {report_data['date']}"

        elif report_type == "2":
            report_content = f"Reporte 2{report_data['date']}"

        elif report_type == "3":
            report_content = f"Reporte 3{report_data['date']}"

        elif report_type == "4":
            report_content = f"Reporte 4{report_data['date']}"

        else:
            return {
                "data": {},
                "message": f"Tipo de reporte no soportado: {report_type}",
                "status": False
            }, 400

        # Generar PDF y guardar o devolver según necesidad
        pdf_filename = f"reporte_{report_type}_{report_data['date']}.pdf"
        pdf_path = f"/ruta/donde/guardar/{pdf_filename}"  # Ajusta esta ruta según tu entorno

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

    '''def get_downloadable(self):
        down = list(self.collection.find({}, {"wid": 0}))
        status = True if down else False
        message = "Descarga encontrada exitosamente" if status else "Descarga no encontrada"
        status_code = 200 if status else 500
        return {
            "data": down,
            "message": message,
            "status": status
        }, status_code'''

    def create_downloadable(self, downloadable: list[Downloadable]):
        result = self.collection.insert_many(downloadable)
        if result.inserted_ids:
            return {
                "data": downloadable,
                "message": "Descarga creada exitosamente",
            }, 201
        else:
            return {
                "data": [],
                "message": "Error al crear descarga",
                "status": False
            }, 500

    def delete_downloadable(self, id: str):
        result = self.collection.delete_one({"id": ObjectId(id)})
        status_code = 200
        if result.deleted_count == 0:
            return {
                "message": "Descarga no encontrada",
                "status": False
            }, 500
        else:
            return {
                "message": "Descarga eliminada con éxito",
                "status": True
            }, status_code

    def update_downloadable(self, id: str = None, title: str = None, new_quantity: int = 0):
        if id:
            reso = self.collection.find_one({"id": ObjectId(id)})
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
            }, 500

        result = self.collection.update_one({"id": ObjectId(reso["id"])}, {"$set": {"stock": new_quantity}})
        if result.modified_count > 0:
            updated_reso = self.collection.find_one({"id": ObjectId(reso["id"])}, {"id": 0})
            return {
                "data": updated_reso,
                "message": "Actualizada con éxito",
                "status": True
            }, 200
        else:
            return {
                "data": {},
                "message": "Error al actualizar",
                "status": False
            }, 500
