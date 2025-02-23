import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src import predict as pred
import logging

logging.basicConfig(level=logging.INFO)

class PredictionData(BaseModel):
    year: int
    month: int
    day: int
    province: int
    fuel_type: int

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Fuel prediction prices in Spain"}

@app.post("/predict/pai")
def predict_pai_model(data:PredictionData):
    year = data.year
    month = data.month
    day = data.day
    province = data.province
    fuel_type = data.fuel_type

    prediction = pred.predict_pai_model(year, month, day, province, fuel_type)

    if prediction == None:
        raise HTTPException(
            status_code=500,
            detail="Ha habido un error con la predicción. Inténtelo de nuevo más tarde."
        )

    return {
        "prediction": prediction[0]
    }

@app.post("/predict/pvp")
def predict_pvp_model(data:PredictionData):
    year = data.year
    month = data.month
    day = data.day
    province = data.province
    fuel_type = data.fuel_type


    prediction = pred.predict_pvp_model(year, month, day, province, fuel_type)

    if prediction == None:
        raise HTTPException(
            status_code=500,
            detail="Ha habido un error con la predicción. Inténtelo de nuevo más tarde."
        )

    return {
        "prediction": prediction[0]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)