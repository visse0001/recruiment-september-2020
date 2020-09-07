import requests

from fastapi import FastAPI

# Start applications
app = FastAPI(
    title='A microservice for data authorization.',
    description='Input: name, email. Output: PASS or FAIL',
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/")
def read_users():
    url = 'http://127.0.0.1:3000/login/'
    r = requests.get(url)

    r = r.text
    return r
