from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db

from sops.schemas import SopCreate, SopRead, SopUpdate
from sops.services  import SopService
router = APIRouter(prefix="/sops", tags=["sops"])


@router.post("/", response_model=SopRead)
def create_sop(data: SopCreate, db: Session = Depends(get_db)):

    service = SopService(db)
    return service.create_sop(data)


@router.get("/", response_model=list[SopRead])
def list_sops(db: Session = Depends(get_db)):
    service = SopService(db)
    return service.list_sops()

@router.get("/{sop_name}", response_model = SopRead)
def get_sop(sop_name:str, db:  Session = Depends(get_db)):
    service = SopService(db)
    return service.get_sop(sop_name)


@router.patch("/{sop_name}", response_model = SopRead)
def update_sop(sop_name : str, data: SopUpdate, db: Session = Depends(get_db)):
    service =  SopService(db)
    return service.update_sop(sop_name,data)


@router.delete("/{sop_name}", status_code=204)
def delete_sation(sop_name : str, db: Session = Depends(get_db)):
    service = SopService(db)
    return service.delete_sop(sop_name)