from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "auth_user"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String, unique=True, index=True)
    last_login = Column(String, index=True)
    is_superuser = Column(Integer, index=True)
    username = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    is_staff = Column(Integer, index=True)
    is_active = Column(Integer, index=True)
    date_joined = Column(String, index=True)
    first_name = Column(String, index=True)

