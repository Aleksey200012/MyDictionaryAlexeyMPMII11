from django.shortcuts import redirect
from django.urls import path
from . import views


urlpatterns = [
    path("", lambda req: redirect("home"), name="home"),
    path("home/", views.home, name="home"),
    path('words_list/', views.words_list, name='words_list'),
    path('add_word/', views.add_word, name='add_word'),
]