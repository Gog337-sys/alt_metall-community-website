from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.basket import BasketCreate, BasketResponse
from app.services.basket_service import BasketService

router = APIRouter(
    prefix="/basket",
    tags=["basket"],
)

def get_basket_service(
    db: Session = Depends(get_db),
) -> BasketService:
    return BasketService(db)

@router.post(
    "/",
    response_model=BasketResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_basket(
    schema: BasketCreate,
    service: BasketService = Depends(get_basket_service),
):
    return service.create_basket(schema)

@router.get(
    "/",
    response_model=list[BasketResponse],
)
def get_baskets(
    service: BasketService = Depends(get_basket_service),
):
    return service.get_baskets()

@router.get("/{basket_id}", response_model=BasketResponse)
def get_basket(basket_id: int, service: BasketService = Depends(get_basket_service)):
    return service.get_basket(basket_id)

@router.delete(
    "/{basket_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_basket(
    basket_id: int,
    service: BasketService = Depends(get_basket_service)
) -> None:
    service.basket_delete(basket_id)