from fastapi import HTTPException

from sqlalchemy.orm import Session

from stations.models import Station
from stations.schemas import StationCreate, StationRead
from robots.models import Robot


class StationService :
    
    def __init__(self,db:Session):
        self.db = db

    def create_station(self,data:StationCreate) -> StationRead : 
        station_data = data.model_dump(exclude = {"robot_name"})
        station = Station(**station_data)
        if data.robot_name :
            robot = self.db.query(Robot).filter(Robot.name == data.robot_name).first()
            if not robot : 
                raise HTTPException(status_code = 404, detail = "robot not found ")
            if robot.station is not None :
                raise HTTPException(status_code = 400, detail = "Robot assigned to another station")
            station.robot = robot  
        self.db.add(station)
        self.db.commit()
        self.db.refresh(station)
        return station 

    def list_stations(self) -> list[StationRead] : 
        stations = self.db.query(Station).all()
        return stations 
    
    def get_station(self,station_name : str) -> StationRead :
        station = self.db.query(Station).filter(Station.name == station_name).first()
        return station 