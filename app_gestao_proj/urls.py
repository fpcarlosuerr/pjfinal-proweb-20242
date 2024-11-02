from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_gestao_proj,name='index_app_gestao_proj'),
]