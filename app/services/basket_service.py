from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.basket import Basket
from app.repository.basket_repository import BasketRepository
from app.schemas.basket import BasketCreate

class BasketService:

    def __init__(self, db:Session):
        self.repository = BasketRepository(db)

    def create_basket(self, schema: BasketCreate):

        basket = Basket(**schema.model_dump())

        return self.repository.create(basket)

    def get_baskets(self) -> list[Basket]:
        return self.repository.get_all()

    def get_basket(self, basket_id: int) -> Basket:
        basket = self.repository.get_by_id(basket_id)

        if basket is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="basket not found",
            )

        return basket

    def basket_delete(self, basket_id: int) -> None:
        basket = self.get_basket(basket_id)

        self.repository.delete(basket)