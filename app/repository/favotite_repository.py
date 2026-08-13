from sqlalchemy.orm import Session
from app.models.favorite import Favorite

class FavoriteRepository:
    def __init__(self, db: Session):
        self.db = db

    def _upsert(self, favorite: Favorite):
        self.db.add(favorite)
        self.db.commit()
        self.db.refresh(favorite)

        return favorite

    def create(self, favorite: Favorite):
        return self._upsert(favorite)

    def update(self, favorite: Favorite):
        return self._upsert(favorite)

    def get_all(self) -> list[Favorite]:
        return self.db.query(Favorite).all()

    def get_by_id(self, favorite_id: int,) -> Favorite | None:
        return self.db.query(Favorite).filter(Favorite.id == favorite_id).first()

    def delete(self, favorite: Favorite) -> None:
        self.db.delete(favorite)
        self.db.commit()
    