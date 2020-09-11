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

    url = f'http://{django_host}:3000/login/'
    r = requests.get(url)
    print(r.text)
    # r.json()

    return str(r.json())
