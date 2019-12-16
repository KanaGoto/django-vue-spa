#!/bin/sh
rm -d -r db.sqlite3
rm -rf apps/products/migrations             
rm -rf apps/users/migrations             
rm -rf apps/reviews/migrations  
rm -rf apps/shopping/migrations  
rm -rf apps/favorites/migrations  
rm -rf apps/users/__pycache__
rm -rf apps/products/__pycache__
rm -rf apps/reviews/__pycache__ 
rm -rf apps/favorites/__pycache__   
rm -rf apps/shopping/__pycache__

python3 manage.py makemigrations users
python3 manage.py makemigrations products
python3 manage.py makemigrations reviews
python3 manage.py makemigrations favorites
python3 manage.py makemigrations shopping

python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
