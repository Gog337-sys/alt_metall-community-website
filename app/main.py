import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI


from app.database import Base, engine
from app.config.config import get_settings
from app.api.items import router as items_router

settings = get_settings()

app = FastAPI()

app.include_router(items_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return{
        "message": f"{settings.app_name} is running"
    }
