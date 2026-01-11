from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
#
def test_api_works():
    response = client.post("/predict", json={"value": "test"})
    assert response.status_code == 200
