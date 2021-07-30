FROM python:3.7
WORKDIR /dockerApplication
COPY requirements.txt /dockerApplication/

RUN pip install --no-cache-dir -r requirements.txt
COPY ./MfsAfricaApi /dockerApplication/
#ENTRYPOINT['entrypoint.sh']
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
#CMD exec gunicorn djangoapp.wsgi:application --bind 0.0.0.0:8000 --workers 3
