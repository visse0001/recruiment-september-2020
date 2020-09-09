import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel

# DATABASE_URL = postgresql+psycopg2://{user}:{password}@{host}:{port}
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@postgres:5432"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

