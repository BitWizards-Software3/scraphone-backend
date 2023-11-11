import pytest
from services.scrap_alibaba import scrape_alibaba, extract_price


def test_extract_price():
    # Prueba un precio único sin guión
    price_text = "100"
    price = extract_price(price_text)
    assert price == 100.0

    # Prueba un rango de precios con guión, debería tomar el precio más bajo
    price_text = "50 - 100"
    price = extract_price(price_text)
    assert price == 50.0

def test_scrape_alibaba():
    # Prueba la función scrape_alibaba con datos de ejemplo
    search_term = "shoes"
    product_data = scrape_alibaba(search_term)

    # Verifica que la lista de productos no esté vacía
    assert product_data

    # Verifica que cada producto tenga los campos esperados
    for product in product_data:
        assert "Product" in product
        assert "Price" in product
        assert "Link" in product
        assert "Image" in product
