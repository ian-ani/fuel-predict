import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

from src import predict as pred

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

def run_prediction(data:PredictionData, model):
    year = data.year
    month = data.month
    day = data.day
    province = data.province
    fuel_type = data.fuel_type

    prediction = pred.predict_model(year, month, day, province, fuel_type, model)

    if prediction == None:
        raise HTTPException(
            status_code=500,
            detail="Error al predecir los datos. Prueba de nuevo más tarde."
        )
    
    logging.info(f"La predicción se ha efectuado correctamente. Resultado: {prediction[0]}")

    return {
        "prediction": round(prediction[0], 2)
    }

@app.get("/")
def index():
    return {"title": "Predicción de los precios del combustible en España.",
            "docs": "/docs - documentación Swagger para probar la API desde el navegador.",
            "web": "Para que la web funcione correctamente, primero debes tener un servidor HTTP o hacer uso de Live Server.",
            "source": "Documentación y código fuente: https://github.com/ian-ani/fuel-predict"}

@app.post("/predict/pai")
def predict_pai_model(data:PredictionData):
    return run_prediction(data, "pai_model.pkl")

@app.post("/predict/pvp")
def predict_pvp_model(data:PredictionData):
    return run_prediction(data, "pvp_model.pkl")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)