from fastapi import FastAPI

from pydantic import BaseModel


class Message(BaseModel):
    first_name: str
    last_name: str
    email: str


app = FastAPI(
    title='A microservice for data authorization.',
    description='Input: first name, last name, email. Output: "PASS" or "FAIL"',
)


@app.post("/check/")
def check(message: Message):
    # result = db.query(models.User).filter(models.User.first_name == message.first_name && models.User.last_name == message.last_name)
    # if len(result) > 0:
    #     return {"message": "PASS"}
    # else:
    #     return {"message": "FAIL"}
    return message