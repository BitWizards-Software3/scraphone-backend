from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la URL de conexión a la base de datos MySQL
#only config Mary userbd is admin1 for other is admin
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://admin1:12345@localhost:3306/scraphone"

# Creación de una instancia del motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()