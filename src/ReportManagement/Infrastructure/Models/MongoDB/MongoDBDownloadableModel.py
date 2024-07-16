from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional


class DownloadoadableModel(BaseModel):
    id: Optional[ObjectId] = Field(default=None, alias="_id")
    type: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: lambda v: str(v)
        }

