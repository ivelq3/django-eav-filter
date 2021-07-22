FROM python:3.8.0-alpine
WORKDIR /usr/src/backend
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers && pip install Pillow
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/backend/requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/backend/
