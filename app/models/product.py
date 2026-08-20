from typing import List, TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.models.category import Category
    from app.models.favorite import Favorite
    from app.models.basket import Basket

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    brand: Mapped[str]
    price: Mapped[int]
    rating: Mapped[int]
    thumbnail: Mapped[str]
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="products")
    favorites: Mapped[List["Favorite"]] = relationship(back_populates="product", cascade="all, delete-orphan")
    basket: Mapped[List["Basket"]] = relationship(back_populates="product", cascade="all, delete-orphan")
