from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from sops.models import Sop
from sops.schemas import SopCreate, SopRead

router = APIRouter(prefix="/sops", tags=["sops"])


@router.post("/", response_model=SopRead)
def create_sop(data: SopCreate, db: Session = Depends(get_db)):
    sop = Sop(**data.model_dump())
    db.add(sop)
    db.commit()
    db.refresh(sop)
    return sop


@router.get("/", response_model=list[SopRead])
def list_sops(db: Session = Depends(get_db)):
    return db.query(Sop).all()
