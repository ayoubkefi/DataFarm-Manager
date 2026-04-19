from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class SopInCollectionItem(BaseModel):
    id : UUID
    name : str
    is_active : bool  
    model_config = ConfigDict(from_attributes=True)


class CollectionItemCreate(BaseModel):
    name : str 
    description : str | None 
    quantity : int | None = None

class CollectionItemUpdate(BaseModel):
    name : str | None = None
    description : str | None 
    quantity : int | None = None

class SopCollectionItemRead(BaseModel):
    
    sop :  SopInCollectionItem
    required_quantity: int 
    model_config = ConfigDict(from_attributes=True)
    

class CollectionItemRead(BaseModel):
    id : UUID
    name : str 
    description : str | None
    quantity :  int 
    created_at : datetime
    updated_at : datetime
    sops : list["SopCollectionItemRead"] = []

    model_config = ConfigDict(from_attributes=True)