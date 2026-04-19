from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

from core.enums import RobotType


class StationCreate(BaseModel):
    name: str
    description: str | None = None
    is_active: bool = True
    robot_name: str | None = None

class StationUpdate(BaseModel):
    name : str | None = None
    description : str | None = None
    is_active : bool | None = None
    robot_name : str | None = None

class RobotInStation(BaseModel):
    id : UUID
    name : str 
    robot_type : RobotType

class StationRead(BaseModel):
    id: UUID
    name: str
    description: str | None
    is_active: bool
    robot :  RobotInStation | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
