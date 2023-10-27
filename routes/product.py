from fastapi import APIRouter
from config.database import conn
from schemas.product import ProductBase
from models.product import product
from sqlalchemy.exc import SQLAlchemyError

product=APIRouter()

