# 🧠 FastAPI Classification App (Dockerized)

This project is a simple **Machine Learning Classification API** built with **FastAPI**. It includes:

- Input validation using **Pydantic**
- A pre-trained **ML classification model**
- Docker support for containerization

---

## 📁 Folder Structure

classification-faastapi-app-simple/



├── app/

    ├── main.py # Entry point of the FastAPI app

    |──data_validation.py     # To validate the data passed in URL Endpoint

    |──model_prediction.py    # To load the model and make Predictions 

    |──0__init__.py  # For making App as package 


├── model/

     ├── iris_model.pkl # Pre-trained ML model for classification

     ├── Model_Trainer.py # Script for loading data Training model and saving model 




├── Dockerfile # Instructions to build the Docker image

├── requirements.txt # Python dependencies

├── README.md 

├── .dockerignore # to ignore some file to send in countainer 




---

## 🚀 What Each File Does

### `app/main.py`
- Initializes the FastAPI app
- make default Route
- make predict Route have features parameter of Inputvalidator Type which is Pydantic inherited class for data validation 



---

### `app/data_validation`
- This file countain InputValidator class that is used as input parameter of Endponint Predict 

### `app/model_prediction`
- This file is responsible for Loading the Trained model From model/iris_model.pkl

### `model/model_trainer.py`
- This file is responsible for Loading the Iris data train the model and save the model 

### `Dockerfile`

- Builds a Docker image for the FastAPI app

Steps:

- Uses a slim Python base image

- Installs dependencies from requirements.txt

- Copies app files into the container

- Runs the FastAPI app using Uvicorn

---



# Running the App with Docker

### 1. Build the Docker image
 
 docker build -t iris-api .
 
### 2. Run the Docker container

docker run -p 8000:8000 iris-api

### 3. Access the API

### Open your browser or use Postman to access:


http://127.0.0.1:8000
or 
    https://localhost:8000



# ✅ Example Request On Postman 

Endpoint:  http://localhost:8000/predict


In raw data select JSON

{

  "sepal_length": 5.1,

  "sepal_width": 3.5,

  "petal_length": 1.4,

  "petal_width": 0.2
  
}


- Response:


{

  "prediction": "setosa"

}
