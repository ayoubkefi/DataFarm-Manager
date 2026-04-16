from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, INTEGER

from db.base import Base
from db.db_mixin import TimestampMixin, UUIDMixin





class CollectionItem(Base, TimestampMixin, UUIDMixin):

    __tablename__ = "collection_items"
    name : Mapped[str] = mapped_column(String, nullable=False,unique=True)
    description : Mapped[str | None] = mapped_column(Text, nullable=True)
    quantity :  Mapped[int | None] = mapped_column(INTEGER, nullable=True,default=1)
    sops: Mapped[list["SopCollectionItem"] | None] = relationship(
        "SopCollectionItem",
        back_populates="collection_item",
        cascade="all, delete-orphan",
    )