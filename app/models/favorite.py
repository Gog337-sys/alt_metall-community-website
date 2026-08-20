from typing import List, Optional, TYPE_CHECKING  # Добавлен TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from app.database import Base

if TYPE_CHECKING:
    from app.models.product import Product

class Favorite(Base):
    __tablename__ = "favorites"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    
    product: Mapped["Product"] = relationship(back_populates="favorites")
