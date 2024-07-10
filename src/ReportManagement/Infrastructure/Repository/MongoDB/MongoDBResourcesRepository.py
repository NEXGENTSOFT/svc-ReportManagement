from bson import ObjectId
from src.ReportManagement.Domain.Ports.ResourcesPort import ResourcesPort
from src.ReportManagement.Domain.Entity.Resources import Resources
from src.ReportManagement.Infrastructure.Models.MongoDB.MongoDBResourcesModel import ResourcesModel

class ResourcesRepository(ResourcesPort):
    def __init__(self):
        self.collection = ResourcesModel.get_collection()

    def get_resources(self):
        resour = list(self.collection.find({}, {"_id": 0}))
        status = True if resour else False
        message = "Recursos encontrados exitosamente" if status else "Recursos no encontrados"
        status_code = 200 if status else 500
        return {
            "data": resour,
            "message": message,
            "status": status
        }, status_code

    def create_resources(self, resources: list[Resources]):
        result = self.collection.insert_many(resources)
        if result.inserted_ids:
            return {
                "data": resources,
                "message": "Recursos creados exitosamente",
            }, 201
        else:
            return {
                "data": [],
                "message": "Error al crear recursos",
                "status": False
            }, 500

    def delete_resources(self, id: str):
        result = self.collection.delete_one({"_id": ObjectId(id)})
        status_code = 200
        if result.deleted_count == 0:
            return {
                "message": "Recurso no encontrado",
                "status": False
            }, 500
        else:
            return {
                "message": "Recurso eliminado con éxito",
                "status": True
            }, status_code

    def update_resources(self, resource_id: str = None, title: str = None, new_quantity: int = 0):
        if resource_id:
            reso = self.collection.find_one({"_id": ObjectId(resource_id)})
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
                "message": "Recurso no encontrado",
                "status": False
            }, 500

        result = self.collection.update_one({"_id": ObjectId(reso["_id"])}, {"$set": {"stock": new_quantity}})
        if result.modified_count > 0:
            updated_reso = self.collection.find_one({"_id": ObjectId(reso["_id"])}, {"_id": 0})
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
