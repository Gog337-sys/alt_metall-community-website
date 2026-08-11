from fastapi import FastAPI


from app.config.config import get_settings
from app.api.items import router as items_router

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)

app.include_router(items_router)

@app.get("/")
def root():
    return{
        "message": f"{settings.app_name} is running"
    }
