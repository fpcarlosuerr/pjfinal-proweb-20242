from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_applocaimoveis,name='index_locaimoveis'),
]