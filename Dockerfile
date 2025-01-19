FROM ubuntu:22.04

USER root
WORKDIR /app

COPY python_practice/ /app/

RUN apt update
RUN apt install -y python3
RUN apt-get install -y vim
