from fastapi import FastAPI
import joblib
import numpy as np
from app.schemas import HeartRequest

app = FastAPI(title="Heart Disease Prediction API")

#load model 

model = joblib.load("model/heart_model_random_forest.joblib")

features_list = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal"
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return{
        "model_type":str(type(model).__name__),
        "features": features_list
    }



@app.post("/predict")
def predict(request: HeartRequest):
    x = np.array([[request.age, request.sex, request.cp, request.trestbps, request.chol,
                   request.fbs, request.restecg, request.thalach, request.exang,
                   request.oldpeak, request.slope, request.ca, request.thal]])
    prediction = model.predict(x)[0]
    return {"heart_disease": bool(prediction)}