FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY ./test.py /test.py


RUN apt install -y apache2

RUN python3 test.py

ENTRYPOINT apachectl -D FOREGROUND
