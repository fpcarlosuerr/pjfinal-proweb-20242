from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_reuniao, name='index_reuniao'),
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('cadastrar_sala/', views.cadastrar_sala, name='cadastrar_sala'),
    path('resevar_sala/', views.resevar_sala, name='resevar_sala'),
    path('cadastrar_equipamento/', views.cadastrar_equipamento, name='cadastrar_equipamento')
]