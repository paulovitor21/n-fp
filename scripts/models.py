from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Date

Base = declarative_base()

class NFPRecord(Base):
    
    __tablename__= 'table_nfp'

    
    id = Column(Integer, primary_key=True, index=True)
    file_date = Column(name="file_date", type_=Date)
    org = Column(name='org', type_=String)
    model_suffix = Column(name='model_suffix', type_=String)
    date = Column(name="date", type_=TIMESTAMP)
    quantity = Column(name="quantity", type_=Integer)
    hash_id = Column(String, unique=True)

