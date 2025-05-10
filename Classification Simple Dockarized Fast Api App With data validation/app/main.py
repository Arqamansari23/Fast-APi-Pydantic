from fastapi import FastAPI
from app.data_validation import IrisInputValidator
from app.model_Prediction import predict_iris_species


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Species Prediction API!"}

@app.post("/predict")
def prediction(features: IrisInputValidator):
    prediction=predict_iris_species(
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    )
    # Convert the prediction to a string for better readability
    prediction = str(prediction)

    return {"Predicted Species is ": prediction}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)