# An application with a microservice for data authorization

Link to the [task](https://github.com/visse0001/recruiment-september-2020/blob/develop/recuriment_task.md).

## Virtual Enviroment
Create a virtual environment: <br/>
`python3.8 -m venv venv`

To activate a venv: <br/>
`source venv/bin/activate`

## Dependencies

[Python 3.8](https://www.python.org/downloads/) <br>
[pip](https://pip.pypa.io/en/stable/installing/) <br>
[Django](https://docs.djangoproject.com/en/3.1/) <br>
[Postgres](https://www.postgresql.org/) <br>
[FastAPI](https://fastapi.tiangolo.com/) <br>

To upgrade existing pip: <br>
`pip install --upgrade pip`

To install dependencies from requirements.txt: <br>
`pip install -r requirements.txt`

## Docker

[Install Docker](https://docs.docker.com/get-docker/)
```
docker -v
Docker version 19.03.5, build 633a0ea

docker-compose -v
docker-compose version 1.25.4, build 8d51620a
```

Build the image:

`docker-compose build`

Fire up cointainers:

`docker-compose up`

or fire up containers in detached mode:

`docker-compose up -d`