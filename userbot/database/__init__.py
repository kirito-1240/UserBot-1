import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from Config import Config

def start() -> scoped_session:
    if "postgres://" in Config.DATABASE_URL:
        database_url = Config.DATABASE_URL.replace("postgres:", "postgresql:")      
    else:
        database_url = Config.DATABASE_URL
    engine = create_engine(database_url)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))
try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    print("DATABASE_URL Is Not Configured.")
    print(str(e))
