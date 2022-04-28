from django.urls import path
from . import views

urlpatter = {
    path("sentiment", views.sentiment),
}