from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from sops.models import Sop
from sops.schemas import SopCreate, SopRead
from sops.services  import SopService
router = APIRouter(prefix="/sops", tags=["sops"])


@router.post("/", response_model=SopRead)
def create_sop(data: SopCreate, db: Session = Depends(get_db)):

    service = SopService(db)
    return service.create_sop(data)


@router.get("/", response_model=list[SopRead])
def list_sops(db: Session = Depends(get_db)):
    service = SopService(db)
    return service.lists_sops()
