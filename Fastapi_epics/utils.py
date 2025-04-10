import pickle
import numpy as np

import joblib

crop_model = joblib.load("Pickle Files/crop_model.pkl")
fertilizer_model = joblib.load("Pickle Files/fertilizer.pkl")


def get_predictions(data: dict):
    crop_input = np.array([
        data["N"],
        data["P"],
        data["K"],
        data["temperature"],
        data["humidity"],
        data["ph"],
        data["rainfall"]
    ]).reshape(1, -1)

    fert_input = np.array([
        data["N"],
        data["P"],  
        data["K"]
    ]).reshape(1, -1)

    crop_pred = crop_model.predict(crop_input)[0]
    fert_pred = fertilizer_model.predict(fert_input)[0]

    return crop_pred, fert_pred
