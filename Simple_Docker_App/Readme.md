# 🚀 Simple FastAPI Dockerized App

This is a minimal example of a FastAPI application running inside a Docker container. It includes two basic endpoints and can be easily extended for larger projects.

---

## 📁 Project Structure

Simple_Docker_App/
│
├── main.py # FastAPI application

├── requirements.txt # Python dependencies

├── Dockerfile # Docker build configuration

└── README.md # Project documentation


## 📦 Requirements

- [Docker](https://www.docker.com/products/docker-desktop) installed and running

---

## 🚧 Setup Instructions

2️⃣ Build the Docker Image

docker build -t simple-fastapi-app .

3️⃣ Run the Docker Container


docker run  -p 8000:8000 simple-fastapi-app

🔍 Available Endpoints

After running the container, open your browser:


Root endpoint:

http://localhost:8000/

Response:

{"message":"Hello from FastAPI!"}


# Some Additional commands

docker ps        # Get container ID

docker stop <container_id>


## View logs:

docker logs <container_id>





