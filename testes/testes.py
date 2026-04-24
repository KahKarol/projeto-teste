from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_obter_data_hora():
    # Coleta a data e hora exatas 
    response = client.get("/agora")
    assert response.status_code == 200
    assert "data" in response.json()
    assert "horario" in response.json()

