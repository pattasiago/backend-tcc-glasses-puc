FROM python:3.11.6-slim-bullseye

WORKDIR /app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

COPY src/ .

RUN pip install --upgrade pip \
    pip install -r ./requirements.txt

CMD ["python", "main.py"]