set -e
python manage.py collectstatic --noninput
uwsgi --socket :8096 --master --enable-threads --module MfsAfricaApi.wsgi
