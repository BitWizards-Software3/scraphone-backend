from sqlalchemy import create_engine, MetaData

# Configuración de la URL de conexión a la base de datos MySQL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://admin1:12345@localhost:3306/scraphone"

# Creación de una instancia del motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creación de una instancia de MetaData
meta = MetaData()

# Establecimiento de una conexión a la base de datos
conn = engine.connect()
print()