from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from operators.schemas import OperatorCreate, OperatorRead, OperatorUpdate
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
    
@router.patch("/{operator_number}",response_model = OperatorRead)
def update_operator(operator_number : int, data : OperatorUpdate, db: Session = Depends(get_db)):
    service = OperatorService(db)
    return service.update_operator(operator_number,data)
    
@router.delete("/{operator_number}", status_code=204) 
def delete_operator(operator_number : int, db: Session = Depends(get_db) ):
    service = OperatorService(db)
    return service.delete_operator(operator_number)

