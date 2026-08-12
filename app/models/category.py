from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.models.product import Product

class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str]

    product: Mapped[List["Product"]] = relationship(back_populates="category")