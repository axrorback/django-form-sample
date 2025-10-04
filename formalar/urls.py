from django.urls import path

from .views import savollar , home

urlpatterns = [
    path('savollar/',savollar),
    path('thank-you/',home),
]