from sqlalchemy.orm import Session
from collection_items.models import CollectionItem
from collection_items.schemas import CollectionItemCreate, CollectionItemRead, CollectionItemUpdate


from core.exceptions import raise_not_found

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
    
    def get_collectionItem(self, collection_item_name: str) -> CollectionItemRead:
        collection_item = self.db.query(CollectionItem).filter(CollectionItem.name == collection_item_name).first()
        if collection_item is None:
            raise_not_found("Collection item",collection_item_name) 
        return collection_item

    def update_collectionItem(self, collection_item_name : str, data: CollectionItemUpdate) -> CollectionItemRead : 
        update_data = data.model_dump(exclude_unset = True)
        collectionItem = self.get_collectionItem(collection_item_name)
        for field, value in update_data.items():
            setattr(collectionItem,field,value)
        self.db.commit()
        self.db.refresh(collectionItem)
        return collectionItem 
    

    def delete_collectionItem(self,item_name : str) -> None : 
        collectionItem = self.get_collectionItem(item_name)
        self.db.delete(collectionItem)
        self.db.commit()
