FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

RUN mkdir -p /var/lib/dbdata/
RUN chmod 777 /var/lib/dbdata/

COPY . /code/