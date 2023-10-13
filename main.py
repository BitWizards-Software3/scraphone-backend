from fastapi import FastAPI
from routes.scrap_router import router

app = FastAPI()

app.include_router(router)