from sqlalchemy import Column, Integer
from config.database import Base, engine


class Patient(Base):
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(255))
    shelf = Column(String(255))
    stock = Column(Integer)
    stock_notification = Column(Integer)   
    existence_notification = Column(Integer)
Base.metadata.create_all(bind=engine)