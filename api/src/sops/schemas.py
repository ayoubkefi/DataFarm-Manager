from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID
from datetime import datetime
from robots.models import RobotType


class CollectionItemInSop(BaseModel):
    id: UUID
    name: str
    description: str | None = None
    quantity: int | None = None

    model_config = ConfigDict(from_attributes=True)

class SopCollectionItemCreate(BaseModel):
    item_name: str
    required_quantity: int = Field(gt=0)


class SopCreate(BaseModel):
    name: str
    description: str | None = None
    is_active: bool = True
    robot_type: RobotType
    collection_items: list[SopCollectionItemCreate] = []


class SopCollectionItemRead(BaseModel):
    collection_item : CollectionItemInSop
    required_quantity: int

    model_config = ConfigDict(from_attributes=True)

    
class SopRead(BaseModel):
    id: UUID
    name: str
    description: str | None
    is_active: bool
    robot_type: RobotType
    collection_items: list[SopCollectionItemRead] = []
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)