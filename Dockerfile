FROM python:3.6-alpine

ARG DB_HOST

ENV DB_HOST $DB_HOST

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["gunicorn"]

CMD ["swagger_server.__main__:app", "-w", "5", "-b", "0.0.0.0:8080", "--log-file=-"]