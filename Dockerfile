FROM python:3.8-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean \
    && apt-get -y install python3-dev libpq-dev

RUN pip install --upgrade pip

COPY ./project/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

COPY ./project/entrypoint.sh ./project
RUN chmod +x /usr/src/app/project/entrypoint.sh

ENTRYPOINT [ "/usr/src/app/project/entrypoint.sh" ]
