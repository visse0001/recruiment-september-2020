from pydantic import BaseModel


class Message(BaseModel):
    first_name: str
    last_name: str
    email: str


class User(BaseModel):
    last_name: str
    email: str
    first_name: str

    class Config:
        orm_mode = True
