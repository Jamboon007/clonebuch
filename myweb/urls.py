from django.urls import path 
from . import views

urlpatterns = [
    path("about", views.index, name="index"),
    path("", views.story, name="story"),
    path("contact", views.contact, name="contact"),

]