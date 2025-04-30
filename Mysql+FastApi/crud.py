# crud.py
# 📦 Purpose: Handle database operations (Create, Read, Update, Delete)

from sqlalchemy.orm import Session
from models import User
from schema import UserCreate

# Create new user
def create_user(db: Session, user: UserCreate):
    new_user = User(**user.model_dump())  # Convert schema to model
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get all users
def get_all_users(db: Session):
    return db.query(User).all()

# Get user by ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Update user
def update_user(db: Session, user_id: int, user_data: UserCreate):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = user_data.name
        user.email = user_data.email
        user.age = user_data.age
        db.commit()
        db.refresh(user)
    return user

# Delete user
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
