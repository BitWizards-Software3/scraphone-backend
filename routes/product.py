from fastapi import APIRouter, HTTPException, Response, Depends, HTTPException, status
from models.product import Product
from starlette.status import HTTP_201_CREATED, HTTP_409_CONFLICT
from config.database import engine
from schemas.product import ProductBase, ProductView 
from sqlalchemy.orm import Session
from config.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Endpoint para agregar productos
@router.post("/products", response_model=None)
def create_product(product: ProductBase, db: Session = Depends(get_db)):
    # Verificar si ya existe un producto con el mismo id
    #existing_prodcut = db.query(Product).filter(Product.id == product.id).first()
    #if existing_prodcut:
    #    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product with this id already exists")

    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

#Endpoint para modificar productos
@router.put("/products/{product_id}", response_model=None)
def update_user(product_id: int, product: ProductBase, db: Session = Depends(get_db)):
    db.query(Product).filter(Product.id == product_id).update(product.dict(exclude_unset=True))
    db.commit()
    updated_product = db.query(Product).filter(Product.id == product_id).first()
    return updated_product
