FROM python:3.6

WORKDIR /manyx_core
COPY . /manyx_core

RUN apt update && apt install -y git python3-pip
RUN pip3 install -r requirements.txt

