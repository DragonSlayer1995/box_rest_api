# syntax=docker/dockerfile:1

FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.main
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD flask run