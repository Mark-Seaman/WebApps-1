# Lesson 4 - Installing Django

## Install Django Libraries

    pip install django
    pip freeze

Make sure that Django is in the list of installed packages.

    Django==4.0.5

## Test your Django Setup

    django-admin startproject MyApp

This should create a bunch of files.  If it doesn't you don't have the setup correct.

Run the web server

    cd MyApp
    python manage.py runserver

Browse to the web page at **http://localhost:8000**

