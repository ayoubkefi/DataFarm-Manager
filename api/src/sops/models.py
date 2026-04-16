from sqlalchemy import String, Boolean, Enum, Text, ForeignKey, INTEGER, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy.dialects.postgresql import UUID 
import uuid 

from collection_items.models import CollectionItem
from db.base import Base
from db.db_mixin import TimestampMixin, UUIDMixin

from robots.models import RobotType



class SopCollectionItem(Base) :
    __tablename__ = "sop_collection_items"
    __table_args__ = (
        CheckConstraint("required_quantity > 0 ",
                         name = "ck_sop_collection_items_required_quantity_positive",
        ),
    )
    sop_id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid = True),
        ForeignKey("sops.id", ondelete="CASCADE"),
        primary_key = True
    )
    
    collection_item_id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid = True),
        ForeignKey("collection_items.id", ondelete = "CASCADE"),
         primary_key=True
    )
    required_quantity : Mapped[int] = mapped_column(INTEGER, nullable=False, default=1)
    sop : Mapped["Sop"] = relationship("Sop", back_populates="collection_items")
    collection_item : Mapped["CollectionItem"] = relationship("CollectionItem", back_populates= "sops")


class Sop(Base, TimestampMixin, UUIDMixin):
    __tablename__ = "sops"

    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text, nullable=True, unique=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    robot_type: Mapped[RobotType] = mapped_column(Enum(RobotType, name="robot_type"), nullable=False)
    collection_items : Mapped[list["SopCollectionItem"]] = relationship(
        "SopCollectionItem",
        back_populates="sop",
        cascade="all, delete-orphan"
    )