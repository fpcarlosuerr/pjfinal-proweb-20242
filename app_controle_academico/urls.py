from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_controle_academico,name='controle_academico'),
]