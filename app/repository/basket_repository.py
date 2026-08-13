from sqlalchemy.orm import Session
from app.models.basket import Basket

class BasketRepository:
    def __init__(self, db: Session):
        self.db = db

    def _upsert(self, basket: Basket):
        self.db.add(basket)
        self.db.commit()
        self.db.refresh(basket)

        return basket

    def create(self, basket: Basket):
        return self._upsert(basket)

    def update(self, basket: Basket):
        return self._upsert(basket)

    def get_all(self) -> list[Basket]:
        return self.db.query(Basket).all()

    def get_by_id(self, basket_id: int,) -> Basket | None:
        return self.db.query(Basket).filter(Basket.id == basket_id).first()

    def delete(self, basket: Basket) -> None:
        self.db.delete(basket)
        self.db.commit()
    