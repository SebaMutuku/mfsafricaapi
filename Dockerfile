FROM python:3.8

#COPY ./requirements.txt entrypoint.sh  /dockerApplication/

RUN mkdir -p /dockerApplication/
WORKDIR /dockerApplication
#ADD . /dockerApplication/
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY MfsAfricaApi .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8096
CMD ["python","manage.py","runserver","0.0.0.0:8097"]
#CMD exec gunicorn -w 4 MfsAfricaApi.wsgi:application --bind 0.0.0.0:8097 --workers 3
#ENTRYPOINT ["entrypoint.sh"]
