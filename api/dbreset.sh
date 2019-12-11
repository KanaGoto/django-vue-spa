#!/bin/sh
rm -d -r db.sqlite3
rm -rf apps/goods/migrations             
rm -rf apps/users/migrations             
rm -rf apps/user_operation/migrations  
rm -rf apps/users/__pycache__
rm -rf apps/goods/__pycache__
rm -rf apps/user_operation/__pycache__    

python3 manage.py makemigrations users
python3 manage.py makemigrations goods
python3 manage.py makemigrations user_operation

python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
