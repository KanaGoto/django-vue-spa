#!/bin/sh
python3 manage.py makemigrations users
python3 manage.py makemigrations goods
python3 manage.py makemigrations user_operation

python3 manage.py migrate
python3 manage.py runserver
