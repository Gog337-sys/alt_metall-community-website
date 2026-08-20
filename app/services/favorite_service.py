from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.favorite import Favorite
from app.repository.favotite_repository import FavoriteRepository
from app.schemas.favorite import FavoriteCreate

class FavoriteService:

    def __init__(self, db: Session):
        self.repository = FavoriteRepository(db)

    def create_favorite(self, schema: FavoriteCreate) -> Favorite:

        favorite = Favorite(**schema.model_dump())

        return self.repository.create(favorite)

    def get_favorites(self) -> list[Favorite]:
        return self.repository.get_all()

    def get_favorite(self, favorite_id: int) -> Favorite:
        favorite = self.repository.get_by_id(favorite_id)

        if favorite is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="favorite not found",
            )
        return favorite

    def delete_favorite(self, favorite_id: int) -> None:
        favorite = self.get_favorite(favorite_id)

        self.repository.delete(favorite)