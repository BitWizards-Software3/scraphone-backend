from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Configuración de la URL de conexión a la base de datos MySQL
#only config Mary userbd is admin1 for other is admin
SQLALCHEMY_DATABASE_URL = "XXX desencriptar la clave de la db" #conectar a la base de datos en la nube
#mysql://root:c156bfc35A3DbEe34GhbAc2A-13Ee413@roundhouse.proxy.rlwy.net:47095/railway

#mysql+pymysql://admin:1234@localhost:3306/scraphone    con base de datos local
# Creación de una instancia del motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

""""
encriptar clave de la base de datos en la nube

1. mmysql://root:c156bfc35A3DbEe34GhbAc2A-13Ee413  
2. zx@roundhouse.proxy.rlwy.net:
3. 12A47095/railway
"""