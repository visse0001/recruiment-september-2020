import json
import requests

from fastapi import FastAPI

# Start applications
app = FastAPI(
    title='A microservice for data authorization.',
    description='Input: first name, last name, email. Output: "PASS" or "FAIL"',
)


@app.post("/check/")
def check():
    # django_host = "localhost"
    # # django_host = "django"
    #
    # url = f'http://{django_host}:3000/user_auth/'
    # r = requests.get(url)
    # print(f'Request: {r}.')

    return 'kotek'
