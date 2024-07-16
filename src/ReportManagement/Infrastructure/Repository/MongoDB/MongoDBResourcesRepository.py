from bson import ObjectId
from pymongo import MongoClient

from src.Database.MongoDB.connection import resource_collection
from src.ReportManagement.Domain.Ports.ResourcesPort import ResourcesPort


class ResourcesRepository(ResourcesPort):
    def __init__(self):
        self.collection = resource_collection

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

    def create_resources(self, resources: list[dict]):
        for resource in resources:
            if 'id' in resource and isinstance(resource['id'], str):
                resource['_id'] = ObjectId(resource.pop('id'))
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
        try:
            result = self.collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count > 0:
                return {
                    "message": "Recurso eliminado con éxito",
                    "status": True
                }, 200
            else:
                return {
                    "message": "Recurso no encontrado",
                    "status": False
                }, 404
        except Exception as e:
            return {
                "message": str(e),
                "status": False
            }, 500

    def update_resources(self, resource_id: str = None, title: str = None, update_data: dict = {}):
        try:
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
