from fastapi import APIRouter, HTTPException
from typing import Dict
from services.scraper_services import scrape_amazon
from services.scrap_aliexpress import scrape_aliexpress

router = APIRouter()


@router.post("/scrape/")
async def scrape_endpoint(search_data: Dict[str, str]):
    # Verifica si el término de búsqueda está presente en los datos
    if "search_term" not in search_data:
        raise HTTPException(status_code=422, detail="Falta el término de búsqueda")
    
    search_term = search_data["search_term"]
    
    # Llama a la función de scraping con el término de búsqueda
    product_data = scrape_amazon(search_term)

    return {"productos": product_data}


@router.post("/scrape_aliexpress/")
async def scrape_endpoint(search_data: Dict[str, str]):
    # Verifica si el término de búsqueda está presente en los datos
    if "search_term" not in search_data:
        raise HTTPException(status_code=422, detail="Falta el término de búsqueda")
    
    search_term = search_data["search_term"]
    
    # Llama a la función de scraping con el término de búsqueda
    product_data = scrape_aliexpress(search_term)

    return {"productos": product_data}