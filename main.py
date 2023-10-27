from fastapi import FastAPI
from routes.scrap_router import router
from routes.product import product
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)



origins = [
    "http://localhost",
    "http://localhost:4200",
    
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product,tags=["product"],prefix="/product")