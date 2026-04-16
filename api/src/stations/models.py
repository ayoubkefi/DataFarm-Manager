import uuid

from sqlalchemy import String, Boolean, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from db.base import Base
from db.db_mixin import TimestampMixin, UUIDMixin


class Station(Base, TimestampMixin, UUIDMixin):
    __tablename__ = "stations"

    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    robot_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("robots.id", ondelete="RESTRICT"),
        nullable=True,
        unique=True,
    )
    robot: Mapped["Robot | None"] = relationship("Robot", back_populates="station")
