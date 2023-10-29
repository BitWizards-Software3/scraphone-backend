import pytest
import requests
from bs4 import BeautifulSoup
from services.scrap_aliexpress import scrape_aliexpress

def test_scrape_aliexpress():
    # Prueba la función scrape_aliexpress con un término de búsqueda de ejemplo
    search_term = "iphone"
    product_data = scrape_aliexpress(search_term)

    # Verifica que la lista de productos no esté vacía
    assert product_data

    # Verifica que cada producto tenga los campos esperados
    for product in product_data:
        assert "Product" in product
        assert "Price" in product
        assert "Link" in product
        assert "Image" in product

        # Verifica que el precio sea un número positivo
        assert isinstance(product["Price"], (int, float)) and product["Price"] >= 0.0

        # Verifica que el enlace sea válido
        assert product["Link"].startswith("https://es.aliexpress.com/")

        # Verifica que la imagen sea válida
        assert product["Image"].startswith("https://")

        # Verifica que el nombre del producto no esté vacío
        assert product["Product"].strip() != ""

    # Prueba adicional: Verifica que se obtengan más de un producto
    assert len(product_data) > 1
