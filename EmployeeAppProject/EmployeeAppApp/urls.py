from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("gotThatInfo/", views.gotThatInfo, name='gotThatInfo'),
]