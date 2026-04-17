from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

from core.enums import RobotType
from robots.schemas import RobotRead


class StationCreate(BaseModel):
    name: str
    description: str | None = None
    is_active: bool = True
    robot_name: str | None = None

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

    class Config:
        from_attributes = True
