from fastapi import FastAPI
import uvicorn


app = FastAPI() 


# hit endpoint http://127.0.0.1:8000/  For home function to Execute

@app.get("/")
def home():
    return {"message": "Hello, World!"}


# hit endpoint http://127.0.0.1:8000/personalized/John  For personalized_greeting function to Execute

@app.get("/personalized/{name}")
def personalized_greeting(name: str):
    return {"message": f"Hello, {name}!"}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

