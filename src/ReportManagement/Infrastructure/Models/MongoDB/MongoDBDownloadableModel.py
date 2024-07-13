from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional


class DownloadoadableModel(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    type: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
