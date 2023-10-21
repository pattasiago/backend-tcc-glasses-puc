FROM python:3.11.6-slim-bullseye

WORKDIR /app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

COPY ./ .

RUN pip install --upgrade pip \
    pip install -r ./src/requirements.txt

CMD ["python", "./src/main.py"]