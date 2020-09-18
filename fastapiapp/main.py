import sqlite3

from fastapi import FastAPI

from pydantic import BaseModel
from starlette.responses import RedirectResponse

app = FastAPI(
    title='A microservice for data authorization.',
    description='Input: first name, last name, email. Output: "PASS" or "FAIL"',
)


class Message(BaseModel):
    first_name: str
    last_name: str
    email: str


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.post("/check", response_model=Message)
def check(message: Message):
    try:
        first_name = message.first_name
        conn = sqlite3.connect('../djangoapp/db.sqlite3')
        cursor = conn.cursor()
        query = """SELECT first_name FROM auth_user WHERE first_name=?"""
        cursor.execute(query, (first_name,))
        result = cursor.fetchone()
        if result:
            return {"message": "PASS"}
        else:
            return {"message": "FAIL"}
        cursor.close()
    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
