import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_process():
    response = client.post("/processes/", json={
        "name": "Processo Teste",
        "description": "Descrição do processo de teste"
    })
    assert response.status_code == 201
    assert response.json()["name"] == "Processo Teste"

def test_get_processes():
    response = client.get("/processes/")
    assert response.status_code == 200
    assert len(response.json()) > 0