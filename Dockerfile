

FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /sloovi_crud


WORKDIR /sloovi_crud


ADD . /sloovi_crud/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD gunicorn sloovi_crud.wsgi:application --bind 0.0.0.0:$PORT