from django.urls import path 
from myweb.views import index

urlpatterns = [
    path("", index, name='index'),
]