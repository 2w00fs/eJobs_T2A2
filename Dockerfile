# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ARG cid
ARG csecret
ARG dbaddress
ARG dbname
ARG dbuser
ARG dbpass

ENV CLIENT_ID $cid
ENV CLIENT_SECRET $csecret
ENV DB_ADDRESS $dbaddress
ENV DB_NAME $dbname
ENV DB_USER $dbuser
ENV DB_PASS $dbpass

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=$PORT", "--cert=adhoc"]

