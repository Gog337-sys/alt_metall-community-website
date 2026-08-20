from pydantic import BaseModel, ConfigDict, Field

class ProductCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1, max_length=200)
    category_id: int = Field()
    brand: str = Field(min_length=1, max_length=200)
    price: int = Field()
    rating: int = Field()
    thumbnail: str = Field(min_length=1, max_length=200)
    favorite: bool = Field(default=None)
    basket: bool = Field(default=None)

class ProductUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, min_length=1, max_length=200)
    category_id: int | None = Field(default=None)
    brand: str | None = Field(default=None, min_length=1, max_length=200)
    price: int | None = Field(default=None)
    rating: int | None = Field(default=None)
    thumbnail: str | None = Field(default=None, min_length=1, max_length=200)
    
class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    category_id: int
    brand: str
    price: int
    rating: int
    thumbnail: str
