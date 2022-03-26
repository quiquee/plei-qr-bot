FROM python:3.9
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /

RUN python -m pip install -r requirements.txt

COPY . /