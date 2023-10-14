import requests
from bs4 import BeautifulSoup
import json

def scrape_alibaba(search_term):
    url = requests.get(f'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={search_term}')
    soup = BeautifulSoup(url.content, 'html.parser')
    
    productos = soup.find_all("div", class_="fy23-search-card fy23-gallery-card m-gallery-product-item-v2 J-search-card-wrapper")  
    product_data = []
    for prod in productos:
        print(productos)
        # Extraer el nombre del producto
        name = prod.find("h2", class_="search-card-e-title").text.strip()
        # Extraer la imagen del producto
        
        # Extraer el precio del producto
        price_text = prod.find("div", class_="search-card-e-price-main").text.strip()
        #price_text = price_text.replace('US', '').replace(',', '')  # Eliminar 'US' y las comas
        #price = float(price_text)  # Convertir el precio a un número
        # Extraer el enlace del producto

        # Añadir el producto a la lista de productos
        product_data.append({
            'Product': name,
            'Price': price_text,
        })

    # Convertir la lista de productos en un objeto JSON y devolverlo
    return product_data
