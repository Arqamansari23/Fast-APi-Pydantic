# This File is responsible for loading the model and making predictions
import joblib
import numpy as np

model=joblib.load("model/iris_model.pkl")


def predict_iris_species(sepal_length, sepal_width, petal_length, petal_width):
    features=np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction=model.predict(features)

    return prediction[0]