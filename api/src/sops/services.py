from sops.models import Sop
from sops.schemas import SopCreate, SopRead

from sqlalchemy.orm import Session

class SopService:
    def __init__(self,db:Session):
        self.db = db

    def create_sop(self,data:SopCreate, db: Session) -> SopRead : 
        sop = Sop(**data.model_dump())
        self.db.add(Sop)
        self.db.commit()
        self.db.refresh(Sop)
        return sop
    
    def lists_sops(self) -> list[SopRead]:
        sops = self.db.query(Sop).all()
        return sops 
    
    def get_sop(self,sop_name:str) -> SopRead :
        sop = self.db.query(Sop).filter(Sop.name == sop_name)
        return sop
    