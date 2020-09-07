import requests
import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse

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
    url = 'http://django:3000/login/'
    r = requests.get(url)
    r.json()
    return JSONResponse(r)
