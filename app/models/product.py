from sqlalchemy import String, Integer, Boolean, Float
from typing import List, Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.category import Category
from app.models.favorite import Favorite
from app.models.basket import Basket

class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String, nullable=False)

    description: Mapped[str] = mapped_column(String, nullable=False)

    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))

    cotegory: Mapped["Category"] = relationship(back_populates="product")

    brand: Mapped[str] = mapped_column(String, nullable=False)

    price: Mapped[int] = mapped_column(Integer, nullable=False)

    rating: Mapped[float] = mapped_column(Float, nullable=False)

    thumbnail: Mapped[str] = mapped_column(String, nullable=False)

    favorite: Mapped[List["Favorite"]] = relationship(back_populates="product", cascade="all, delere-orphan")

    basket: Mapped[List["Basket"]] = relationship(back_populates="product", cascade="all, delere-orphan")