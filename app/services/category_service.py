from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.category import Category
from app.repository.category_repository import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryUpdate

class CategoryService:

    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def create_category(self, schema: CategoryCreate):

        category = Category(
            title=schema.title,
        )

        return self.repository.create(category)

    def get_categores(self) -> list[Category]:
        return self.repository.get_all()

    def get_category(self, category_id: int) -> Category:
        category = self.repository.get_by_id(category_id)

        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="net",
            )
        return category

    def update_category(self,
                        categore_id: int,
                        schema: CategoryUpdate,
                        ) -> None:
        category = self. get_category(categore_id)

        update_data = schema.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(category, key, value)

        return self.repository.update(category)

    def delete_category(self, category_id: int) -> None:
        category = self.get_category(category_id)

        
        if len(category.products) > 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Нельзя удалить категорию, содержащую товары. Сначала перенесите или удалите товары."
            )

        self.repository.delete(category)