sleep 3

export SCHOOL_ADMIN_PASSWORD=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 32)

python manage.py makemigrations
python manage.py migrate
python manage.py seed_db

python -m gunicorn --workers=4 --timeout 0 --preload --bind 0.0.0.0:8000 TheFinder.wsgi:application
#python manage.py runserver 0.0.0.0:8000