# Lesson 5 - Your first app

## Create a new project

    mkdir 05/Superhero

    cd 05/Superhero

    django-admin startproject config .

Run the web server

    python manage.py runserver

Browse to the web page at **http://localhost:8000**


## Create a Django App Component

    python manage.py startproject hero


config/settings.py

    # Handle all URL requests made to web server
    ALLOWED_HOSTS = ['*']

    # Enable data the Profile app
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'hero',
    ]    

config/urls.py

    from django.http import HttpResponse
    from django.urls import path

    def index(request):
        return HttpResponse("<h1>Superhero</h1><p>I love my heroes.</p>")

    urlpatterns = [
        path('', index),
    ]


## Test your Superhero app

Run the web server

    python manage.py runserver

Browse to the web page at **http://localhost:8000**


## Debug within Visual Studio

