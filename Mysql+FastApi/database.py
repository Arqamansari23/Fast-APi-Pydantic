# database.py
# 📦 Purpose: Set up the MySQL database connection using SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Hardcoded MySQL DB credentials (for learning/testing)
DATABASE_URL = "mysql+pymysql://root:arqam@localhost:3306/fastapi_db"

# Create DB engine
engine = create_engine(DATABASE_URL)

# SessionLocal will be used for DB operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy models
Base = declarative_base()
