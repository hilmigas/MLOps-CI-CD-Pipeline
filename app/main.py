from fastapi import FastAPI
from app.logic import stable_hash

app = FastAPI()

@app.post("/predict")
def predict(data: dict):
    return {"result": stable_hash(data["value"])}
