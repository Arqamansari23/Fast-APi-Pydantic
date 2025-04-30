from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()

# In-memory user database
fake_users_db = {}

class User(BaseModel):
    name: str
    email: str
    age: int

# GET: Retrieve user by name
@app.get("/users/{name}")
def get_user(name: str):
    user = fake_users_db.get(name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# POST: Create new user
@app.post("/users/")
def create_user(user: User):
    if user.name in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    fake_users_db[user.name] = user
    return {"message": "User created", "user": user}

# PUT: Fully update a user
@app.put("/users/{name}")
def update_user(name: str, updated_user: User):
    if name not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    fake_users_db[name] = updated_user
    return {"message": "User updated", "user": updated_user}

# PATCH: Partially update user (e.g., just email)
@app.patch("/users/{name}")
def partial_update_user(name: str, email: Optional[str] = None):
    if name not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    if email:
        fake_users_db[name].email = email
    return {"message": "User partially updated", "user": fake_users_db[name]}

# DELETE: Delete a user
@app.delete("/users/{name}")
def delete_user(name: str):
    if name not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del fake_users_db[name]
    return {"message": f"User '{name}' deleted"}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)