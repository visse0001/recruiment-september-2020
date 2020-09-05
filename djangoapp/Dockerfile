FROM python:3.8.2-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app



# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY .env.dev /app/.env.dev

# copy entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY . /app/

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
