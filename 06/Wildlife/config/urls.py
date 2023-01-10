from animals.views import AnimalsView
from django.urls import path


urlpatterns = [
    path('', AnimalsView.as_view()),
]
