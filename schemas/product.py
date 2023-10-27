from sqlalchemy import Table, Column, Integer, String
from config.database import meta, engine

# Creación de una tabla llamada "product"
product = Table(
    "product",        # Nombre de la tabla
    meta,             # Instancia de MetaData
    Column("id", Integer, primary_key=True),  # Columna de clave primaria
    Column("name", String(255)),             # Columna para el nombre del producto
    Column("description", String(255)),      # Columna para la descripción del producto
    Column("shelf", String(255)),            # Columna para la ubicación del producto
    Column("stock", Integer),               # Columna para la cantidad de stock
    Column("stock_notification", Integer),  # Columna para el umbral de notificación de stock bajo
    Column("existence_notification", Integer)  # Columna para el umbral de notificación de existencia baja
)

# Creación de la tabla en la base de datos
meta.create_all(engine)
