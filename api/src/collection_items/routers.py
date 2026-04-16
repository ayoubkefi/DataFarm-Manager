from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from collection_items.schemas import CollectionItemCreate, CollectionItemRead
from collection_items.services import CollectionItemService
from db.session import get_db
router = APIRouter(prefix="/collection_items", tags=["collection_items"])

@router.post("/",response_model=CollectionItemRead)
def create_collection_item(data: CollectionItemCreate,db: Session = Depends(get_db) ):
    service = CollectionItemService(db)
    return service.create_collectionItem(data)

@router.get("/", response_model= list[CollectionItemRead])
def list_collection_items(db:Session = Depends(get_db)):
    service = CollectionItemService(db)
    return service.list_collectionItems()

@router.get("/{collection_item_name}",response_model=CollectionItemRead)
def get_collection_item(item_name : str, db:Session = Depends(get_db)):
    service = CollectionItemService(db)
    return service.get_collectionItem(item_name)
