# docke file for the project
FROM python:3.6

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /manyx_core
COPY . /manyx_core

RUN pip3 install -r requirements.txt

