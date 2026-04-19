from sqlalchemy.orm import Session

from stations.models import Station
from stations.schemas import StationCreate, StationRead

class StationService :
    
    def __init__(self,db:Session):
        self.db = db

    def create_station(self,data:StationCreate) -> StationRead : 
        station = Station(**data.model_dump()) 
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