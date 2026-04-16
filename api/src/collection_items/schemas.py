from pydantic import BaseModel
from uuid import UUID
from datetime import datetime



class SopCollectionItemRead(BaseModel):
    sop_id : UUID
    required_quantity: int 
    class config :
            from_attributes = True 
class CollectionItemCreate(BaseModel):
    name : str 
    description : str | None 
    quantity : int | None = None

class CollectionItemRead(BaseModel):
    id : UUID
    name : str 
    description : str | None
    quantity :  int 
    created_at : datetime
    updated_at : datetime
    sops : list["SopCollectionItemRead"] = []

    class Config:
        from_attributes = True