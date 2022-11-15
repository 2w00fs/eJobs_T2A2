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
ARG insec
ARG relax

ENV CLIENT_ID $cid
ENV CLIENT_SECRET $csecret
ENV DB_ADDRESS $dbaddress
ENV DB_NAME $dbname
ENV DB_USER $dbuser
ENV DB_PASS $dbpass
ENV OAUTHLIB_INSECURE_TRANSPORT $insec
ENV OAUTHLIB_RELAX_TOKEN_SCOPE $relax

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000" ]