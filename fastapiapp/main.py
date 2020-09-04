from fastapi import FastAPI

# Start applications
app = FastAPI(
    title='A microservice for data authorization.',
    description='Input: name, email. Output: PASS or FAIL',
)
