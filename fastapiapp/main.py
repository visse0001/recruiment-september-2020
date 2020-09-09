import requests

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from fastapi_sqlalchemy import DBSessionMiddleware  # middleware helper
from fastapi_sqlalchemy import db  # an object to provide global access to a database session


# Start applications
app = FastAPI(
    title='A microservice for data authorization.',
    description='Input: first name, last name, email. Output: "PASS" or "FAIL"',
)

app.add_middleware(DBSessionMiddleware, db_url="postgresql+psycopg2://postgres:postgres@postgres:5432")

@app.get("/users/")
def get_users():
    url = 'http://172.31.0.4:3000/login/'
    # url = 'http://django:3000/login/'
    r = requests.get(url)
    # r.raise_for_status() return <Response [400]>

    r.json()

    return JSONResponse(content=r)
