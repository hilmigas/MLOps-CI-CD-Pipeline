import requests

response = requests.post(
    "http://localhost:8000/predict",
    json={"value": "abc"}
)

assert response.status_code == 200
print("Smoke test passed")
