from sops.models import Sop, SopCollectionItem
from sops.schemas import SopCreate, SopRead, SopUpdate
from collection_items.models import CollectionItem
from fastapi import HTTPException
from sqlalchemy.orm import Session


class SopService:
    def __init__(self,db:Session):
        self.db = db

    def create_sop(self,data:SopCreate) -> SopRead : 
        sop_data  = data.model_dump(exclude={"collection_items"})
        sop = Sop(**sop_data)
        if data.collection_items : 
                for item in data.collection_items :
                    collection_item = self.db.query(CollectionItem).filter(CollectionItem.name == item.item_name).first()
                    if collection_item is None :
                        raise HTTPException(status_code = 404, detail = f"item {item.item_name} not found ")
                    if item.required_quantity <= 0 :
                         raise HTTPException(status_code=400 , detail= f" Invalid Request, Expected positive quantity  got {collection_item.quantity}")
                    sop_collection_item = SopCollectionItem(
                        collection_item=collection_item,  
                        required_quantity=item.required_quantity  
                    )
                    sop.collection_items.append(sop_collection_item)
        self.db.add(sop)
        self.db.commit()
        self.db.refresh(sop)
        return sop
    
    def lists_sops(self) -> list[SopRead]:
        sops = self.db.query(Sop).all()
        return sops 
    
    def get_sop(self,sop_name:str) -> SopRead :
        sop = self.db.query(Sop).filter(Sop.name == sop_name).first()
        return sop
    
    def update_sop(self, sop_name : str, data: SopUpdate) -> SopRead : 
        update_data = data.model_dump(exclude_unset = True)
        sop = self.get_sop(sop_name)
        for field, value in update_data.items():
            setattr(sop,field,value)
        self.db.commit()
        self.db.refresh(sop)
        return sop 
    

    def delete_sop(self,sop_name : str) -> None : 
        sop = self.get_sop(sop_name)
        self.db.delete(sop)
        self.db.commit()
