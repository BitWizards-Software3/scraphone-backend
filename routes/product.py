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

# Endpoint para obtener información sobre un producto específico por su ID
@router.get("/products/{product_id}", response_model=ProductView)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    print(product.name)

    # Crear una instancia de ProductView con los campos correspondientes
    product_view = ProductView(
        name=product.name,
        description=product.description,
        shelf=product.shelf,
        stock=product.stock,
        stock_notification=product.stock_notification,
        existence_notification=product.existence_notification,
        id=product.id
    )

    return product_view

# Endpoint para obtener la lista de todos los productos
@router.get("/products", response_model=list[ProductView])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    product_views = [ProductView(
        name=product.name,
        description=product.description,
        shelf=product.shelf,
        stock=product.stock,
        stock_notification=product.stock_notification,
        existence_notification=product.existence_notification,
        id=product.id
    ) for product in products]

    return product_views

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

# Endpoint para eliminar productos
@router.delete("/products/{product_id}", response_model=None)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    # Buscar el producto en la base de datos
    product = db.query(Product).filter(Product.id == product_id).first()
    
    # Verificar si el producto existe
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    
    # Eliminar el producto de la base de datos
    db.delete(product)
    db.commit()
    
    return None
