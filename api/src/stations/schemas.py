from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class StationCreate(BaseModel):
    name: str
    description: str | None = None
    is_active: bool = True
    robot_id: UUID | None = None


class StationRead(BaseModel):
    id: UUID
    name: str
    description: str | None
    is_active: bool
    robot_id: UUID | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
