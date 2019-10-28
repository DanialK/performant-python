FROM ubuntu:18.04

RUN apt-get update \
	&& apt install -y software-properties-common libev-dev libevdev2 python3.7-dev python3.7-venv python3-pip

RUN mkdir -p /opt/app

WORKDIR /opt/app

COPY ./ ./

RUN python3.7 -m venv venv

RUN /opt/app/venv/bin/pip install --upgrade pip
RUN /opt/app/venv/bin/pip install -r requirements.txt

EXPOSE 8080

CMD PYTHONPATH=./ /opt/app/venv/bin/python services/sentiment_tensorflow_aiohttp/server.py
