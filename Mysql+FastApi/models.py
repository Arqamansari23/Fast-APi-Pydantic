# models.py
# 📦 Purpose: Define the database table structure using SQLAlchemy models

from sqlalchemy import Column, Integer, String
from database import Base

# Define User table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, index=True)
    age = Column(Integer)
