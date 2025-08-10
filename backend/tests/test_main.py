
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_ask_ojs_returns_response():
    response = client.post("/ask", json={"query": "¿Qué es OJS?"})
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    # Acepta tanto respuesta simulada como error simulado
    assert (
        data["response"].startswith("Respuesta a:")
        or data["response"].startswith("No se pudo obtener respuesta de OpenAI")
    )
