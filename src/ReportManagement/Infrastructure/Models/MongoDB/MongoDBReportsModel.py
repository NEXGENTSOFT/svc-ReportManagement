from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

class ReportsModel(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    title: Optional[str] = None
    descrip: Optional[str] = None
    image: Optional[str] = None
    drawing: Optional[str] = None
    measurements: Optional[str] = None
    type: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
