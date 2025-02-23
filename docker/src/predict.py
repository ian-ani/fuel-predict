import pickle
from sklearn.tree import DecisionTreeRegressor
import os
import logging

# ------------
from sklearn.preprocessing import LabelEncoder # no se si este hace falta de momento
le = LabelEncoder()
# ------------

logging.basicConfig(level=logging.INFO)

model_folder = "model"

def load_pvp_model():
    model_path = os.path.join(model_folder, "pvp_model.pkl")
    
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

def load_pai_model():
    model_path = os.path.join(model_folder, "pai_model.pkl")

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

def predict_pvp_model(year, month, day, province, fuel_type):
    pvp_model = load_pvp_model()

    try:
        result = pvp_model.predict([[year, month, day, province, fuel_type]])
        return result
    except Exception as e:
        logging.error(f"Ha ocurrido un error en la predicción: {e}.")
        return None

def predict_pai_model(year, month, day, province, fuel_type):
    pai_model = load_pai_model()

    try:
        result = pai_model.predict([[year, month, day, province, fuel_type]])
        return result
    except Exception as e:
        logging.error(f"Ha ocurrido un error en la predicción: {e}.")
        return None