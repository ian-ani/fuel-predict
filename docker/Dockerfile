FROM python:3.12.7-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN apk add --no-cache build-base
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt > install.log 2>&1 || tail -n 20 install.log

COPY ./api ./api
COPY ./dataset ./dataset
COPY ./model ./model
COPY ./src ./src

CMD ["uvicorn", "api.api:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]