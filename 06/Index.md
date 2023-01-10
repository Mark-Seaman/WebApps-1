# Lesson 6 - Build a view

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

## Create a Template with HTML

hero/templates/hero.html

    '''
    <h1>Superhero</h1>
    <p>I love all kinds of heroes</p>
    <ul>
        <li>Bears</li>
        <li>Fish</li>
        <li>Birds</li>
        <li>Lions</li>
    </ul>
    '''

## Create a View in Python

hero/views.py

    class HeroView(TemplateView):
        template_name = 'hero.html'


## Create a URL route to the View

config/urls.py

    from django.urls import path
    from .views import HeroView

    urlpatterns = [
        path('', HeroView.as_view()),
    ]


## Test your Superhero app

Run the web server

    python manage.py runserver

Browse to the web page at **http://localhost:8000**


## Debug within Visual Studio


