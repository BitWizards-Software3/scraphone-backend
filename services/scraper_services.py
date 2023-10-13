from bs4 import BeautifulSoup
from selenium import webdriver

def scrape_amazon(search_term):
    # URL de Amazon con el término de búsqueda
    url = f"https://www.amazon.in/s?k={search_term}&crid=2M096C61O4MLT&qid=1653308124&sprefix={search_term.replace(' ', '+')}"

    # Inicializa el navegador (en este caso, Chrome)
    driver = webdriver.Chrome()

    driver.get(url)

    # Extrae la colección de resultados
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Lista para almacenar los datos de los productos
    product_data = []

    for item in soup.find_all("div", class_="s-result-item"):
        name = item.find("span", class_="a-size-medium a-color-base a-text-normal")
        if name is not None:
            name = name.text
        else:
            name = ""

        url = item.find("a", class_="a-link-normal a-text-normal")
        if url is not None:
            url = url["href"]
        else:
            url = ""

        price = item.find("span", class_="a-offscreen")
        if price is not None:
            price = price.text
        else:
            price = ""

        rating = item.find("span", class_="a-icon-alt")
        if rating is not None:
            rating = rating.text
        else:
            rating = ""

        review_count = item.find("div", class_="a-section a-text-center")
        if review_count is not None:
            review_count = review_count.text
        else:
            review_count = ""

        product_data.append({
            "Nombre del Producto": name,
            "URL": url,
            "Precio": price,
            "Calificación": rating,
            "Cantidad de Reseñas": review_count
        })

    # Cierra el navegador cuando hayas terminado
    driver.quit()

    return product_data