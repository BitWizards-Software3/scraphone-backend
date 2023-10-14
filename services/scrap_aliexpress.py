import requests
from bs4 import BeautifulSoup
import json

def buscar_producto(producto):
    url = requests.get(f'https://es.aliexpress.com/w/wholesale-{producto}.html')
    soup = BeautifulSoup(url.content, 'html.parser')

    productos = soup.find_all("a", class_="manhattan--container--1lP57Ag cards--gallery--2o6yJVt search-card-item")  # Asegúrate de que estas clases sean correctas
    lista_productos = []
    for prod in productos:
        # Extraer el nombre del producto
        name = prod.find("h1", class_="manhattan--titleText--WccSjUS").text.strip()
        # Extraer el precio del producto
        price = prod.find("div", class_="manhattan--price--WvaUgDY").text.strip()
        # Extraer el enlace del producto
        link = prod['href']
        if link.startswith("//"):
            link = "https:" + link

        # Añadir el producto a la lista de productos
        lista_productos.append({
            'Product': name,
            'Price': price,
            'Link': link
        })

    # Convertir la lista de productos en un objeto JSON y devolverlo
    return json.dumps(lista_productos, ensure_ascii=False)