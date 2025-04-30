from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import uvicorn

app = FastAPI()

# Define the request model using Pydantic
class User(BaseModel):
    name: str = Field(min_length=3, max_length=50)  # Name must be between 3 and 50 characters
    email: EmailStr
    age: Optional[int] = Field(None, ge=18, description="Must be 18 or older") # Age must be 18 or older (can be None) its optional

# Route to create a new user
@app.post("/create_user/")
async def create_user(user: User):
    return {
        "message": "User created successfully",
        "user_data": user
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# hit endpoint http://127.0.0.1:8000/create_user/  For create_user function to Execute
# send a POST request with JSON body like:


'''{
  "name": "Bob",
  "email": "bob@example.com",
  "age": 22
###} '''

