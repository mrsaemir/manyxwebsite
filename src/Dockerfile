# docke file for the project
FROM python:3.6

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /manyx_core
COPY . /manyx_core

RUN mkdir -p media
RUN mkdir -p static

EXPOSE 8000

RUN pip3 install -r requirements.txt

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]
