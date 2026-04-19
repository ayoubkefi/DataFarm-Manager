from fastapi import HTTPException

from sqlalchemy.orm import Session

from stations.models import Station
from stations.schemas import StationCreate, StationRead, StationUpdate
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
        if not station:
            raise HTTPException(status_code=404, detail=f"Station '{station_name}' not found")

        return station 
    
    def update_station(self, station_name : str, data: StationUpdate) -> StationRead : 
        update_data = data.model_dump(exclude_unset = True, exclude={"robot_name"})
        station = self.get_station(station_name)
        for field, value in update_data.items():
            setattr(station,field,value)
        if "robot_name"  in data.model_fields_set : 
            if data.robot_name is None :
                station.robot = None 
            else :
                robot = self.db.query(Station).filter(Station.name == data.station_name).first()
                if not robot : 
                    raise HTTPException(status_code=404, detail="Station not found ")
                if robot.station is not None and robot.station.name != station_name: 
                    raise HTTPException(status_code=400, detail ="Robot already assigned to another station ")
                station.robot = robot

        self.db.commit()
        self.db.refresh(station)
        return station 
    

    def delete_station(self,station_name : str) -> None : 
        station = self.get_station(station_name)
        self.db.delete(station)
        self.db.commit()
