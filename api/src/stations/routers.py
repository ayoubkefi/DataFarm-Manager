from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from stations.schemas import StationCreate, StationRead, StationUpdate
from stations.services import StationService


router = APIRouter(prefix="/stations", tags=["stations"])


@router.post("/", response_model=StationRead)
def create_station(data: StationCreate, db: Session = Depends(get_db)):
    service = StationService(db)
    return service.create_station(data)


@router.get("/", response_model=list[StationRead])
def list_stations(db: Session = Depends(get_db)):
    service = StationService(db)
    return service.list_stations()


@router.get("/{station_name}", response_model=StationRead)
def get_station(station_name: str, db: Session = Depends(get_db)):
    service = StationService(db)
    return service.get_station(station_name)    

@router.patch("/{station_name}", response_model = StationRead)
def update_station(station_name : str, data: StationUpdate, db: Session = Depends(get_db)):
    service =  StationService(db)
    return service.update_station(station_name,data)


@router.delete("/{station_name}", status_code=204)
def delete_station(station_name : str, db: Session = Depends(get_db)):
    service = StationService(db)
    return service.delete_station(station_name)