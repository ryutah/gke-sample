FROM python:3.6.4-alpine

COPY ./requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY ./ /app

WORKDIR /app

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8080"]
