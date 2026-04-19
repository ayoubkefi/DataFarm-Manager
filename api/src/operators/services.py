from sqlalchemy.orm import Session 
from operators.models import Operator
from operators.schemas import OperatorRead, OperatorCreate, OperatorUpdate
from fastapi import HTTPException

class OperatorService:
    
    def __init__(self,db:Session):
        self.db = db
    def create_operator(self, data:  OperatorCreate) ->  OperatorRead :
        operator = Operator(**data.model_dump())
        self.db.add(operator)
        self.db.commit()
        self.db.refresh(operator)
        return operator
    
    def list_operators(self) -> list[OperatorRead] : 
        operators = self.db.query(Operator).all()
        return operators 
    
    def get_operator(self,operator_number :int ) -> OperatorRead :
        operator = self.db.query(Operator).filter(Operator.operator_number == operator_number).first()
        if not operator : 
            raise HTTPException(status_code=404, detail = "Operator not found ")
        return operator
    
    def update_operator(self, operator_number : int, data: OperatorUpdate) -> OperatorRead : 
        operator = self.get_operator(operator_number)
        update_data = data.model_dump(exclude_unset = True)
        for field, value in update_data.items() : 
            setattr(operator,field,value)
        self.db.commit()
        self.db.refresh(operator)
        return operator 
    
    def delete_operator(self,operator_number : int) -> None :
        operator = self.get_operator(operator_number)
        self.db.delete(operator)
        self.db.commit()