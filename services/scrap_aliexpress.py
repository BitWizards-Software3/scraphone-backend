import requests
from bs4 import BeautifulSoup
import json

def scrape_aliexpress(search_term):
    url = requests.get(f'https://es.aliexpress.com/w/wholesale-{search_term}.html')
    soup = BeautifulSoup(url.content, 'html.parser')

    productos = soup.find_all("a", class_="manhattan--container--1lP57Ag cards--gallery--2o6yJVt search-card-item")  
    product_data = []
    for prod in productos:
        # Extraer el nombre del producto
        name = prod.find("h1", class_="manhattan--titleText--WccSjUS").text.strip()
        # Extraer la imagen del producto
        img_tag = prod.find("img", class_="manhattan--img--36QXbtQ product-img")
        if img_tag is not None:
            image = "https:" + img_tag['src']
        else:
            image = 'Not found'
        # Extraer el precio del producto
        price = prod.find("div", class_="manhattan--price-sale--1CCSZfK").text.strip()
        # Extraer el enlace del producto
        link = prod['href']
        if link.startswith("//"):
            link = "https:" + link

        # Añadir el producto a la lista de productos
        product_data.append({
            'Product': name,
            'Price': price,
            'Link': link,
            'Image': image
        })

    # Convertir la lista de productos en un objeto JSON y devolverlo
    return product_data


