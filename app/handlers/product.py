from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.services.product_service import ProductService

router = APIRouter(
    prefix="/product",
    tags=["product"],
)

def get_product_server(
    db: Session = Depends(get_db),
) -> ProductService:
    return ProductService(db)

@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_product(
    schema: ProductCreate,
    service: ProductService = Depends(get_product_server),
):
    return service.create_product(schema)

@router.get(
    "/",
    response_model=list[ProductResponse],
)
def get_products(
    service: ProductService = Depends(get_product_server),
):
    return service.get_products()

@router.get(
    "/{product_id}",
    response_model=ProductResponse,
)
def get_product(
    product_id: int,
    service: ProductService = Depends(get_product_server),
):
    return service.get_product(product_id)

@router.patch(
    "/{product_id}",
    response_model=ProductResponse,
)
def update_product(
    product_id: int,
    schema: ProductUpdate,
    service: ProductService = Depends(get_product_server),
):
    return service.update_product(product_id, schema)

@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_product(
    product_id: int,
    service: ProductService = Depends(get_product_server)
) -> None:
    service.delete_product(product_id)