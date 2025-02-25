import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src import predict as pred
import logging

logging.basicConfig(level=logging.INFO)

#pydantic
class PredictionData(BaseModel):
    year: int
    month: int
    day: int
    province: int
    fuel_type: int

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def index():
    return {"message": "Predicción de los precios del combustible en España."}

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
            detail="Error al predecir los datos. Prueba de nuevo más tarde."
        )
    
    logging.info(f"La predicción se ha efectuado correctamente. Resultado: {prediction[0]}")

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
            detail="Error al predecir los datos. Prueba de nuevo más tarde."
        )
    
    logging.info(f"La predicción se ha efectuado correctamente. Resultado: {prediction[0]}")

    return {
        "prediction": prediction[0]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)