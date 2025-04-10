from pydantic import BaseModel

# Input schema for the API
class InputFeatures(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

# Output schema for the API
class PredictionResult(BaseModel):
    recommended_crop: str
    recommended_fertilizer: str
