FROM python:3.12.7-alpine

WORKDIR /app

COPY ./requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

COPY ./api ./api
COPY ./dataset ./dataset
COPY ./model ./model
COPY ./src ./src