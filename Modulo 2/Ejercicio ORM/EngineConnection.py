from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://postgres:yiyito2920@localhost:5432/postgres', echo=False)

Base = declarative_base()

inspector = inspect(engine)

Session = sessionmaker(bind=engine)
session = Session()
