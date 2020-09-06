from typing import Optional

from fastapi import FastAPI

# Start applications
app = FastAPI(
    title='A microservice for data authorization.',
    description='Input: name, email. Output: PASS or FAIL',
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{first_name}/{last_name}/{email}")
def read_users(first_name: str, last_name: str, email: str):
    return {f'First name: {first_name}, last name: {last_name}, email: {email}'}
