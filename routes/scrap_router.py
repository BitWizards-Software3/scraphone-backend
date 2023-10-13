from fastapi import APIRouter
from services.scraper_services import scrape_amazon

router = APIRouter()


@router.post("/scrape/")
async def scrape_endpoint(search_term: str):
    product_data = scrape_amazon(search_term)
    return {"productos": product_data}