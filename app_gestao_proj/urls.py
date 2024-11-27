from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_gestao_proj,name='base_app_gestao'),

    # urls para membros 
    path('membro/cadastrar', views.cadastrar_membros, name='cadastrar_membros'),
    path('membro/alterar/<int:id>/', views.cadastrar_membros, name='editar_membros'),
    path('membro/excluir/<int:id>/', views.excluir_membros, name='excluir_membros'),
    path('membros/', views.listar_membros, name='listar_membros'),

    # # urls para projeto
    # path('')
]