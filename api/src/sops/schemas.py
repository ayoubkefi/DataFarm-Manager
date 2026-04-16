from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from robots.models import RobotType
from collection_items import CollectionItem

class SopCollectionItemCreate(BaseModel):
    collection_item_id: UUID
    required_quantity: int = Field(gt=0)

class SopCollectionItemRead(BaseModel):
    collection_item_id: UUID
    required_quantity: int

    class Config:
        from_attributes = True

class SopCreate(BaseModel):
    name: str
    description: str | None = None
    is_active: bool = True
    robot_type: RobotType
    collection_items: list[SopCollectionItemCreate] = []


class SopRead(BaseModel):
    id: UUID
    name: str
    description: str | None
    is_active: bool
    robot_type: RobotType
    collection_items: list[SopCollectionItemRead] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True