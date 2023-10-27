from sqlalchemy import Table,Column,Integer,String
from config.database import meta,engine

product=  Table( "product",meta,Column("id",Integer,primary_key=True)
              ,Column("name",String(255))
              ,Column("description",String(255))
              ,Column("shelf",String(255))
              ,Column("stock",Integer)
              ,Column("stock_notification",Integer)
              ,Column("existence_notification",Integer),)


meta.create_all(engine)