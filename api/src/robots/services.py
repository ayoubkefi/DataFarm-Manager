from sqlalchemy.orm import Session
from robots.models import Robot
from robots.schemas import RobotCreate, RobotRead
from fastapi import HTTPException



class RobotService:
    def __init__(self, db: Session):
        self.db = db

    def create_robot(self, data: RobotCreate) -> RobotRead:
        robot = Robot(**data.model_dump())
        self.db.add(robot)
        self.db.commit()
        self.db.refresh(robot)
        return robot

    def list_robots(self) -> list[RobotRead]:
        robots = self.db.query(Robot).all()
        return robots

    def get_robot(self, robot_name: str) -> RobotRead:
        robot = self.db.query(Robot).filter(Robot.name == robot_name).first()
        if not robot:
            raise HTTPException(status_code=404, detail="Robot not found")
        return robot