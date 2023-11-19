# Little-Lemon-Web-Application
# steps to tun website

pip install django

django-admin startproject little_lemon_project

cd little_lemon_project

python manage.py startapp little_lemon_app



python manage.py makemigrations
python manage.py migrate

python manage.py runserver
