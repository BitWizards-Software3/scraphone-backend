from sqlalchemy import Column, Integer, String
from config.database import Base, engine

# Creación de una tabla llamada "product"
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(255))
    shelf = Column(String(255))
    stock = Column(Integer)
    stock_notification = Column(Integer)
    existence_notification = Column(Integer)


# Creación de la tabla en la base de datos
Base.metadata.create_all(bind=engine)