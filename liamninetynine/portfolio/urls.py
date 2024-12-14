from django.urls import path
from . import views

#To access it in a browser, we need to map it to a URL - and for this we need to define a URL configuration, or “URLconf” for short. 

urlpatterns = [
    path("", views.index, name="index"),
]