from django.urls import path
from . import views

urlpatterns = [
    path("", views.audiotogesture, name='home'),
]
