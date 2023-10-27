from fastapi import APIRouter
from sqlalchemy.orm import Session
from config.database import SessionLocal


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()