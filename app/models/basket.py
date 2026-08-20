from typing import List, Optional, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from app.models.product import Product

class Basket(Base):
    __tablename__ = "basket"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    quantity: Mapped[int] = mapped_column(default=1)

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id")) 

    product: Mapped["Product"] = relationship(back_populates="basket")