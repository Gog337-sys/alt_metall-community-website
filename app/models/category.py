from typing import List, TYPE_CHECKING  # Добавлен TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


if TYPE_CHECKING:
    from app.models.product import Product

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]

    products: Mapped[List["Product"]] = relationship(back_populates="category")
