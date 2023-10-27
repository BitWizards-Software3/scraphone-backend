from pydantic import BaseModel
"""
    Clase ProductBase - Define un modelo de datos para productos utilizando Pydantic.

    Atributos:
    - name (str): El nombre del producto.
    - description (str): La descripción del producto.
    - shelf (str): La ubicación del producto en el estante o local.
    - stock (int): La cantidad de stock disponible del producto.
    - stock_notification (int): Umbral de notificación de stock bajo.
    - existence_notification (int): Umbral de notificación de existencia baja.
"""
class ProductBase(BaseModel):
    name: str
    description: str
    shelf: str
    stock: int
    stock_notification : int  
    existence_notification :int