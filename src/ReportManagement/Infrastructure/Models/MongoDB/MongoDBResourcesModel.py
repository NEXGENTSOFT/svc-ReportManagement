from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
class ResourcesModel(BaseModel):
    def __init__(self, id=None, title=None, description=None):
        self.id = id
        self.title = title
        self.description = description

    def to_dict(self):
        return {
             "_id": self.id,
            "title": self.title,
            "description": self
                }

