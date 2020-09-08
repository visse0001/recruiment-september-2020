import requests

from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Start applications
app = FastAPI(
    title='A microservice for data authorization.',
    description='Input: first name, last name, email. Output: "PASS" or "FAIL"',
)


@app.get("/users/")
def read_users():
    url = 'http://172.31.0.4:3000/login/'
    # url = 'http://django:3000/login/'
    r = requests.get(url)
    # r.raise_for_status()
    # [WIP] <Response [400]>

    r.json()

    return JSONResponse(content=r)
