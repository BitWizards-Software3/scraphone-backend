from fastapi import FastAPI
from routes import scrap_router

app = FastAPI()

app.include_router(scrap_router)