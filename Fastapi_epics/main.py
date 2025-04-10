from fastapi import FastAPI
from schemas import InputFeatures, PredictionResult
from utils import get_predictions

app = FastAPI(title="Crop & Fertilizer Recommendation API")

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Crop & Fertilizer Recommendation API 🚀"}

# Prediction route
@app.post("/predict", response_model=PredictionResult)
def predict(data: InputFeatures):
    crop, fertilizer = get_predictions(data.dict())
    return PredictionResult(
        recommended_crop=crop,
        recommended_fertilizer=fertilizer
    )
