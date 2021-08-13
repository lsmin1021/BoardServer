# api/urls.py

from django.urls import path, include
from .views import HelloAPI, postAPI

urlpatterns = [
    path("hello/", HelloAPI),
    path("post/", postAPI),
]