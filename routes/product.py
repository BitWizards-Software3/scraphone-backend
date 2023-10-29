from fastapi import APIRouter
from config.database import conn
from schemas.product import product
from models.product import ProductBase
from sqlalchemy.exc import SQLAlchemyError

product=APIRouter()

