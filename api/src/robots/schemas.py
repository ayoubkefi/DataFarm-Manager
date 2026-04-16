from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from robots.models import RobotType


class RobotCreate(BaseModel):
    name: str
    robot_type: RobotType


class RobotRead(BaseModel):
    id: UUID
    name: str
    robot_type: RobotType
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
