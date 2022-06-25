FROM python:3.10-slim-buster
WORKDIR /app
RUN mkdir -p /app
COPY app/requirements.txt /app
RUN pip install -r requirements.txt
