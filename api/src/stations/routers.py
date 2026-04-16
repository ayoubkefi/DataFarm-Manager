from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from stations.models import Station
from stations.schemas import StationCreate, StationRead
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
