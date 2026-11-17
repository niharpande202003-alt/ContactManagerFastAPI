from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from .config import settings

import os 

database_url=settings.DATABASE_URL

engine=create_engine(database_url)

LocalSession= sessionmaker(autocommit=False, autoFlush=False, bind=engine)

def getDatabase():

    db=LocalSession()

    try:
        yield db

    finally:
        db.close()


Base= declarative_base()
