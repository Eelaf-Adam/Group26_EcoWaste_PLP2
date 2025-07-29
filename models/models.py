from sqlalchemy import column, Integer, String, ForeignKey, Sequence, create_engine
from sqlachemy.com import sessinmkare, relationship, declarative_base 

engine = create_engine('sqllite://orm.db')

Session = sessionmaker(bind=engine)
session = session()

