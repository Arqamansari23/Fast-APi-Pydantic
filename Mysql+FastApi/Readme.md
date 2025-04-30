# 🚀 FastAPI + MySQL CRUD App



This is a simple CRUD (Create, Read, Update, Delete) project using FastAPI, MySQL, SQLAlchemy, and Pydantic v2 (no .env used).

# 📁 Project Folder Structure

MysqlFastApi/
│
├── database.py       # Sets up MySQL database connection using SQLAlchemy
├── models.py         # Defines database models (tables)
├── schemas.py        # Defines request and response models using Pydantic
├── crud.py           # Contains the core CRUD logic
├── main.py           # Initializes FastAPI app and API routes



# 🛠️ Step-by-Step Setup

### 1. Create a MySQL Database
Use MySQL Workbench or CLI to create a database (e.g., fastapi_db).

Note down your DB credentials.

### 2. Set up database.py
Create a SQLAlchemy database connection using your DB credentials.

Set up the session and base class for models.

#### 3. Set up models.py
Define your table structure using SQLAlchemy ORM.

Example: User model with fields like id, name, email, and age.

### 4. Set up schemas.py
Create Pydantic models for:

Incoming data (e.g., UserCreate)

Response data (e.g., UserResponse)

Use Pydantic v2 model_config = {"from_attributes": True} to enable ORM parsing.

### 5. Set up crud.py
Implement functions for:

Creating a user

Fetching all users

Fetching a user by ID

Updating a user

Deleting a user

### 6. Set up main.py
Initialize the FastAPI app.

Create database tables on startup.

Define endpoints:

POST /users/ → Create user

GET /users/ → List users

GET /users/{id} → Get user by ID

PUT /users/{id} → Update user

DELETE /users/{id} → Delete user

### ▶️ Run the App
bash
Copy
Edit
uvicorn main:app --reload
Visit the API docs at:
http://127.0.0.1:8000/docs

### ✅ Requirements
Python 3.10+

FastAPI

SQLAlchemy

pymysql

Pydantic v2

Install dependencies:


pip install fastapi sqlalchemy pymysql pydantic uvicorn