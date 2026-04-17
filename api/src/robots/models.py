import enum

from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base
from db.db_mixin import TimestampMixin, UUIDMixin
from core.enums import RobotType


class Robot(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "robots"

    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    robot_type: Mapped[RobotType] = mapped_column(Enum(RobotType, name="robot_type"), nullable=False)
    station: Mapped["Station"] = relationship("Station", back_populates="robot", uselist=False)
