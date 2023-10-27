from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://admin1:12345@localhost:3306/scraphone"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
meta=MetaData()
conn=engine.connect()