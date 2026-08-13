from pydantic import BaseModel, ConfigDict, Field

from app.schemas.product import ProductResponse

class CategoryCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)

class CategoryUpdate(BaseModel):
    title: str | None= Field(default=None, min_length=1, max_length=200)

class CategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    product: list[ProductResponse]