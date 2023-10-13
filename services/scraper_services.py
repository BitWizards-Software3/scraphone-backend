from bs4 import BeautifulSoup
from selenium import webdriver

def scrape_amazon(search_term):
    # URL de Amazon con el término de búsqueda
    url = f"https://www.amazon.com/s?k={search_term}&crid=2M096C61O4MLT&qid=1653308124&sprefix={search_term.replace(' ', '+')}"

    # Inicializa el navegador (en este caso, Chrome)
    driver = webdriver.Chrome()

    driver.get(url)

    # Extrae la colección de resultados
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Lista para almacenar los datos de los productos
    product_data = []

    for item in soup.find_all("div", class_="s-result-item"):
        name = item.find("span", class_="a-size-medium a-color-base a-text-normal")
        name = name.text[:10] if name else ""

        url_element = item.find("a", class_="a-link-normal s-no-outline")
        url = url_element["href"] if url_element else ""

        price = item.find("span", class_="a-offscreen")
        price = price.text if price else ""

        rating = item.find("span", class_="a-icon-alt")
        rating = rating.text if rating else ""
    

        # Verifica si al menos uno de los campos importantes no está vacío
        if name and url:
            product_data.append({
                "Nombre del Producto": name,
                "URL": f'<a href="{url}">Enlace</a>',
                "Precio": price,
                "Calificación": rating,
            })

    # Cierra el navegador cuando hayas terminado
    driver.quit()

    return product_data