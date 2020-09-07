# An application with a microservice for data authorization

Link to the [task](https://github.com/visse0001/recruiment-september-2020/blob/develop/recuriment_task.md).

## Virtual Enviroment
Create a virtual environment: <br/>
`python3.8 -m venv venv`

To activate a venv: <br/>
`source venv/bin/activate`

To upgrade existing pip: <br>
`pip install --upgrade pip`

To install dependencies from requirements.txt in: djangoapp and fastapiapp: <br>
```
cd djangoapp
pip install -r requirements.txt
cd ..
cd fastapiapp
pip install -r requirements.txt
```

## Dependencies

[Python 3.8](https://www.python.org/downloads/) <br>
[pip](https://pip.pypa.io/en/stable/installing/) <br>
[Django](https://docs.djangoproject.com/en/3.1/) <br>
[Postgres](https://www.postgresql.org/) <br>
[FastAPI](https://fastapi.tiangolo.com/) <br>

## Docker

[Install Docker](https://docs.docker.com/get-docker/)
```
docker -v
Docker version 19.03.5, build 633a0ea

docker-compose -v
docker-compose version 1.25.4, build 8d51620a
```

If you want to build and run containers - you can do it in two ways:

Build and run containers: <br>
`docker-compose up -d --build`

Or

Build the image: <br>
`docker-compose build`

Fire up cointainers: <br>
`docker-compose up`

Or fire up containers in detached mode: <br>
`docker-compose up -d`

## Database: postgres (Django, docker-compose)

To make migrations and migrate: <br>
```
docker-compose exec django python manage.py makemigrations
docker-compose exec django python manage.py migrate
```

To create superuser: <br>
`docker-compose exec django python manage.py createsuperuser`

## Register and login user in the Django app

Go to http://localhost:3000/register <br> and register a new user. <br>
Try to remember first name, last name, email and password. <br>

After logging in you should see something like that: <br>
`{\"first_name\": \"John\", \"last_name\": \"Doe\", \"email\": \"john@doe.com\"}`

## Authenticate in the FastApi app

[WIP]



