from django.http import HttpResponse
from django.urls import path


def index(request):
    return HttpResponse("<h1>Wildlife</h1><p>I love animals</p>")


urlpatterns = [
    path('', index),
]
