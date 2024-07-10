from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

class ReportsModel(BaseModel):
    def __init__(self, id=None, tile=None, descrip=None, image=None, drawing=None,measurements=None, type=None ):
        self.id = id
        self.title = tile
        self.descrip = descrip
        self.image = image
        self.drawing = drawing
        self.measurements = measurements
        self.type = type

    def to_dict(self):
        return {
          "_id": self.id,
            "title": self.title,
            "descripción": self.descrip,
            "image": self.image,
            "drawing": self.drawing,
            "measurements": self.measurements,
            "type": self.type
        }
