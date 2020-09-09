import sqlalchemy
from sqlalchemy import create_engine, databases
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@postgres:5432"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
