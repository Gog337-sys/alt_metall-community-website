import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
import uvicorn
from app.database import Base, engine

from app.models.category import Category
from app.models.product import Product
from app.models.favorite import Favorite
from app.models.basket import Basket
from app.models.users import User


from app.handlers.product import router as product_router
from app.handlers.auth import router as auth_router
from app.handlers.users import router as users_router
from app.handlers.favorite import router as favorite_router
from app.handlers.category import router as category_router
from app.handlers.basket import router as basket_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(product_router)
app.include_router(favorite_router)
app.include_router(category_router)
app.include_router(basket_router)
app.include_router(auth_router)
app.include_router(users_router)

@app.get("/")
def root():
    return{
        "message running"
    }

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)