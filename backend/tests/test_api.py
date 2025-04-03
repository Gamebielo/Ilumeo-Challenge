import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_sem_filtros():
    response = client.get("/conversao/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "data" in response.json()[0]

def test_get_por_canal():
    response = client.get("/conversao/?canal=MOBILE")
    assert response.status_code == 200
    for item in response.json():
        assert item["canal"] == "MOBILE"

def test_get_por_data():
    response = client.get("/conversao/?data_inicio=2025-03-01&data_fim=2025-03-31")
    assert response.status_code == 200
    for item in response.json():
        assert "2025-03-01" <= item["data"] <= "2025-03-31"

def test_get_canal_inexistente():
    response = client.get("/conversao/?canal=inexistente")
    assert response.status_code == 200
    assert response.json() == []

def test_get_data_invalida():
    response = client.get("/conversao/?data_inicio=abc")
    assert response.status_code == 422
