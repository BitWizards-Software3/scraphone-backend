from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    shelf: str
    stock: int
    stock_notification : int  
    existence_notification :int

