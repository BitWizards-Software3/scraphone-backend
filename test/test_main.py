import pytest
from fastapi.testclient import TestClient
from main import app  # Asegúrate de importar tu aplicación FastAPI desde su ubicación

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}