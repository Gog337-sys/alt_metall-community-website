from pydantic import BaseModel, ConfigDict, Field

from app.schemas.product import ProductResponse

class FavoriteCreate(BaseModel):
    product_id: int = Field(default=None)

class FavoriteUpdate(BaseModel):
    product_id: int | None = Field(default=None)

class FavoriteResponce(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    product: ProductResponse