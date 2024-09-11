from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.story, name="story"),
    path("contact", views.contact, name="contact"),

]