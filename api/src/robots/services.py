from sqlalchemy.orm import Session
from robots.models import Robot
from robots.schemas import RobotCreate, RobotRead, RobotUpdate
from core.exceptions import raise_conflict, raise_not_found
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
                raise_not_found("station",  data.station_name)
            if station.robot is not None :
                raise_conflict("Station already assigned to another robot ")

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
            raise_not_found("robot", robot_name)
        return robot
    
    def update_robot(self,robot_name: str, data: RobotUpdate ) -> RobotRead :
        update_data = data.model_dump(exclude_unset = True, exclude={"station_name"})
        robot = self.get_robot(robot_name)
        for field, value in update_data.items():
            setattr(robot,field,value)
        if "station_name"  in data.model_fields_set : 
            if data.station_name is None :
                robot.station = None 
            else :
                station = self.db.query(Station).filter(Station.name == data.station_name).first()
                if not station : 
                    raise_not_found("station",  data.station_name)
                if station.robot is not None and station.robot.name != robot_name : 
                    raise_conflict("Station already assigned to another robot ")
                robot.station = station

        self.db.commit()
        self.db.refresh(robot)
        return robot 
    
    def delete_robot(self,robot_name: str ) -> None : 
        robot = self.get_robot(robot_name)
        self.db.delete(robot)
        self.db.commit()