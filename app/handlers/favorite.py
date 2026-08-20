from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.favorite import FavoriteCreate, FavoriteResponce
from app.services.favorite_service import FavoriteService

router = APIRouter(
    prefix="/favorite",
    tags=["favorite"],
)

def get_favorite_service(
    db: Session = Depends(get_db),
) -> FavoriteService:
    return FavoriteService(db)

@router.post(
    "/",
    response_model=FavoriteResponce,
    status_code=status.HTTP_201_CREATED,
)
def create_favorite(
    schema: FavoriteCreate,
    service: FavoriteService = Depends(get_favorite_service),
):
    return service.create_favorite(schema)

@router.get(
    "/",
    response_model=list[FavoriteResponce],
)
def get_favorites(
    service: FavoriteService = Depends(get_favorite_service),
):
    return service.get_favorites()

@router.delete(
    "/{favorite_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_favorite(
    favorite_id: int,
    service: FavoriteService = Depends(get_favorite_service),
) -> None:
    service.delete_favorite(favorite_id)