from sqlalchemy.orm import Session
from robots.models import Robot
from robots.schemas import RobotCreate, RobotRead
from fastapi import HTTPException

from stations.models import Station


class RobotService:
    def __init__(self, db: Session):
        self.db = db

    def create_robot(self, data: RobotCreate) -> RobotRead:
        robot_data = data.model_dump(exclude={"station_name"})
        robot = Robot(**robot_data)

        if data.station_name:
            station = self.db.query(Station).filter(Station.name == data.station_name).first()
            if not station : 
                    raise HTTPException(status_code=404, detail="Station not found ")
            if station.robot is not None :
                 raise HTTPException(status_code=400, detail="Station assigned to another robot")

            robot.station = station         
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