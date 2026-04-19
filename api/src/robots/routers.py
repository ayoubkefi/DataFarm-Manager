from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from robots.schemas import RobotCreate, RobotRead, RobotUpdate
from robots.services import RobotService

router = APIRouter(prefix="/robots", tags=["robots"])


@router.post("/", response_model=RobotRead)
def create_robot(data: RobotCreate, db: Session = Depends(get_db)):
    service = RobotService(db)
    return service.create_robot(data)


@router.get("/", response_model=list[RobotRead])
def list_robots(db: Session = Depends(get_db)):
    service = RobotService(db)
    return service.list_robots()


@router.get("/{robot_name}", response_model=RobotRead)
def get_robot(robot_name: str, db: Session = Depends(get_db)):
    service = RobotService(db)
    return service.get_robot(robot_name)

@router.patch("/{robot_name}", response_model = RobotRead)
def update_robot(robot_name : str, data: RobotUpdate, db: Session = Depends(get_db)):
    service =  RobotService(db)
    return service.update_robot(robot_name,data)

@router.delete("/{robot_name}",status_code=204)
def delete_robot(robot_name : str, db:Session = Depends(get_db)):
    service = RobotService(db)
    return service.delete_robot(robot_name)