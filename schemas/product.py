from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    shelf: str
    stock: int
    stock_notification: bool  
    existence_notification: bool

class ProductView(ProductBase):
    id: int 