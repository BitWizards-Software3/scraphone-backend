from fastapi import FastAPI
from routes.scrap_router import router as scrape
from routes.product import router as product
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(product)
app.include_router(scrape)



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

app.include_router(product,tags=["product"])
app.include_router(scrape,tags=["scrap"])