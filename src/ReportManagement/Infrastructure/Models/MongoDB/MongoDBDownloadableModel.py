from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional


class DownloadoadableModel(BaseModel):
    def __init__(self, id=None,type=None):
        self.id = id
        self.type = type

    def to_dict(self):
        return {
            "_id": self.id,
            "type": self.type
        }
