from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.models.product import Product
from sqlalchemy import ForeignKey

class Favorite(Base):
    __tablename__ = "favorite"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    product: Mapped[List["Product"]] = relationship(back_populates="favorite")