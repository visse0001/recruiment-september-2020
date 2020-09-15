from pydantic import BaseModel


class Message(BaseModel):
    first_name: str
    last_name: str
    email: str
