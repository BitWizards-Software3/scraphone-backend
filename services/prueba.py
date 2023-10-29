import requests
from bs4 import BeautifulSoup
import json

def scrape_aliexpress(search_term, num_pages):
    all_product_data = []  # Lista para almacenar todos los datos de productos

    for page in range(1, num_pages + 1):
        url = f'https://es.aliexpress.com/w/wholesale-{search_term}.html?SearchText={search_term}&page={page}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        productos = soup.find_all("a", class_="manhattan--container--1lP57Ag cards--gallery--2o6yJVt search-card-item")
        product_data = []

        for prod in productos:
            # Procesar y obtener datos de productos (nombre, imagen, precio, enlace)
            name = prod.find("h1", class_="manhattan--titleText--WccSjUS").text.strip()
            img_tag = prod.find("img", class_="manhattan--img--36QXbtQ product-img")
            if img_tag is not None:
                image = img_tag['src']
                image = 'https:' + image
            else:
                image = 'Not found'
            price_elem = prod.find("div", class_="manhattan--price--WvaUgDY")
            if price_elem is not None:
                price_text = price_elem.text.strip()
                price_text = price_text.replace('COP', '').replace(',', '')  # Eliminar 'COP' y las comas
                price = float(price_text)  # Convertir el precio a un número
            else:
                price = None  # Precio no encontrado

            link = prod['href']
            if link.startswith("//"):
                link = "https:" + link

            product_data.append({
                'Product': name,
                'Price': price,
                'Link': link,
                'Image': image
            })

        # Agregar los datos de la página actual a la lista general
        all_product_data.extend(product_data)

    # Devolver la lista completa de datos de productos
    return all_product_data

num_pages_to_scrape = 1  # Cambia este valor según cuántas páginas desees scrapear
results = scrape_aliexpress("iphone", num_pages_to_scrape)

# Imprimir los resultados o procesarlos como desees
for i, product in enumerate(results, start=1):
    print(f'Producto {i}:')
    print(f'Nombre: {product["Product"]}')
    print(f'Precio: {product["Price"]}')
    print(f'Enlace: {product["Link"]}')
    print(f'Imagen: {product["Image"]}')