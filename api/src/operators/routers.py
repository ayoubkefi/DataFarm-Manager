from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from operators.models import Operator
from operators.schemas import OperatorCreate, OperatorRead
from operators.services import OperatorService

router = APIRouter(prefix="/operators", tags=["operators"])


@router.post("/", response_model=OperatorRead)
def create_operator(data: OperatorCreate, db: Session = Depends(get_db)):
    service = OperatorService(db)
    return service.create_operator(data)


@router.get("/", response_model=list[OperatorRead])
def list_operators(db: Session = Depends(get_db)):
    service = OperatorService(db)
    return service.list_operators()


@router.get("/{operator_number}", response_model=OperatorRead)
def get_operator(operator_number: int, db: Session = Depends(get_db)):
    service = OperatorService(db)
    return service.get_operator(operator_number)
    
