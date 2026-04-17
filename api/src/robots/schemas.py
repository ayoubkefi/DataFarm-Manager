from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import TYPE_CHECKING

from datetime import datetime
from robots.models import RobotType

class StationInRobot(BaseModel):
    
    id : UUID
    name :str 
    is_active : bool 
    model_config = ConfigDict(from_attributes=True)


class RobotCreate(BaseModel):
    name: str
    robot_type: RobotType
    station_name : str | None = None

 
class RobotRead(BaseModel):
    id: UUID
    name: str
    robot_type: RobotType
    station : StationInRobot | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
