
web: gunicorn demo.wsgi

release: python manage.py makemigrations --noinput
release: python manage.py colectstatic --noinput

release: python manage.py migrate --noinput


