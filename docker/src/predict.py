import pickle
import os
import logging

logging.basicConfig(level=logging.INFO)

model_folder = "model"

def load_model(model_file):
    model_path = os.path.join(model_folder, model_file)
    
    try:
        with open(model_path, "rb") as file:
            loaded_model = pickle.load(file)
            logging.info("El modelo se ha cargado correctamente.")
            return loaded_model
    except FileNotFoundError:
        logging.error(f"No se ha podido encontrar el archivo {model_path}.")
    except IOError:
        logging.error(f"No se ha podido leer el archivo {model_path}.")
    except pickle.UnpicklingError:
        logging.error(f"No se ha podido deserializar el modelo {model_path}.")
    except Exception as e:
        logging.error(f"Ha ocurrido un error {e}.")

    return None

def predict_model(year, month, day, province, fuel_type, model_file):
    model = load_model(model_file)

    try:
        result = model.predict([[year, month, day, province, fuel_type]])
        return result
    except Exception as e:
        logging.error(f"Ha ocurrido un error en la predicción: {e}.")
        return None
