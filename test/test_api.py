from fastapi.testclient import TestClient
from main import app  # Asegúrate de importar tu aplicación FastAPI

client = TestClient(app)

def test_scrape_endpoint():
    # Prueba la ruta /scrape/
    response = client.post("/scrape/", json={"search_term": "laptop"})
    assert response.status_code == 200
    data = response.json()
    assert "productos" in data

def test_scrape_aliexpress_endpoint():
    # Prueba la ruta /scrape_aliexpress/
    response = client.post("/scrape_aliexpress/", json={"search_term": "phone"})
    assert response.status_code == 200
    data = response.json()
    assert "productos" in data

def test_scrape_alibaba_endpoint():
    # Prueba la ruta /scrape_alibaba/
    response = client.post("/scrape_alibaba/", json={"search_term": "shoes"})
    assert response.status_code == 200
    data = response.json()
    assert "productos" in data

def test_scrape_both_endpoints():
    # Prueba la ruta /scrape_both/
    response = client.post("/scrape_both/", json={"search_term": "camera"})
    assert response.status_code == 200
    data = response.json()
    assert "productos" in data