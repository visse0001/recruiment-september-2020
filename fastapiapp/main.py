import json
import requests

from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse

# Start applications
app = FastAPI(
    title='A microservice for data authorization.',
    description='Input: first name, last name, email. Output: "PASS" or "FAIL"',
)


@app.get("/check/")
def check():
    django_host = "localhost"
    # django_host = "django"

    url = f'http://{django_host}:3000/user_auth/'
    r = requests.get(url)

    user_data = json.load(r)

    first_name = user_data['first_name']
    last_name = user_data['last_name']
    email = user_data['email']



    return r
