from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime


class OperatorCreate(BaseModel):
    full_name: str
    email: EmailStr
    operator_number: int
    is_active: bool = True


class OperatorRead(BaseModel):
    id: UUID
    full_name: str
    email: EmailStr
    operator_number: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
