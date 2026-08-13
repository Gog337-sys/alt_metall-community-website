from pydantic import BaseModel, Field, ConfigDict

from app.schemas.product import ProductResponse

class BasketCreate(BaseModel):
    quantity: int = Field(default=None)
    product_id: int = Field(default=None)

class BasketUpdate(BaseModel):
    quantity: int | None = Field(default=None)
    product_id: int | None = Field(default=None)

class BasketResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    quantity: int
    product_id: int
    product: ProductResponse