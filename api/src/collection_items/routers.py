from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from collection_items.schemas import CollectionItemCreate, CollectionItemRead, CollectionItemUpdate
from collection_items.services import CollectionItemService
from db.session import get_db
router = APIRouter(prefix="/collection_items", tags=["collection_items"])

@router.post("/",response_model=CollectionItemRead)
def create_collection_item(data: CollectionItemCreate,db: Session = Depends(get_db) ):
    service = CollectionItemService(db)
    return service.create_collection_item(data)

@router.get("/", response_model= list[CollectionItemRead])
def list_collection_items(db:Session = Depends(get_db)):
    service = CollectionItemService(db)
    return service.list_collection_items()

@router.get("/{collection_item_name}", response_model=CollectionItemRead)
def get_collection_item(collection_item_name: str, db: Session = Depends(get_db)):
    service = CollectionItemService(db)
    return service.get_collection_item(collection_item_name)


@router.patch("/{collection_item_name}", response_model = CollectionItemRead)
def update_collection_item(collection_item_name : str, data: CollectionItemUpdate, db: Session = Depends(get_db)):
    service =  CollectionItemService(db)
    return service.update_collection_item(collection_item_name,data)


@router.delete("/{collection_item_name}", status_code=204)
def delete_sation(collection_item_name : str, db: Session = Depends(get_db)):
    service = CollectionItemService(db)
    return service.delete_collection_item(collection_item_name)