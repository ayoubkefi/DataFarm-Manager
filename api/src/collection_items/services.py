from sqlalchemy.orm import Session
from collection_items.models import CollectionItem
from collection_items.schemas import CollectionItemCreate, CollectionItemRead
from fastapi import HTTPException

class CollectionItemService :

    def __init__(self, db:Session):
        self.db  = db
    
    def create_collectionItem(self, data:CollectionItemCreate) -> CollectionItemRead :
        collection_item = CollectionItem(**data.model_dump())
        self.db.add(collection_item)
        self.db.commit()
        self.db.refresh(collection_item)
        return collection_item

    def list_collectionItems(self) -> list[CollectionItem] :
        collection_items = self.db.query(CollectionItem).all()
        return collection_items
    
    def get_collectionItem(self,item_name : str ) -> CollectionItemRead :
        collection_item = self.db.query(CollectionItem).filter(CollectionItem.name == item_name)  
        return collection_item
    