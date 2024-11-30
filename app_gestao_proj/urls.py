from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.app_gestao_proj,name='base_app_gestao'),
    path('login/', auth_views.LoginView.as_view(template_name='app_gestao_proj/login.html'), name='login'),

    # urls para membros 
    path('membro/cadastrar', views.cadastrar_membros, name='cadastrar_membros'),
    path('membro/alterar/<int:id>/', views.cadastrar_membros, name='editar_membros'),
    path('membro/excluir/<int:id>/', views.excluir_membros, name='excluir_membros'),
    path('membros/', views.listar_membros, name='listar_membros'),

    # urls para equipes
    path('equipe/criar', views.criar_equipes, name='criar_equipes'),
    path('equipe/alterar/<int:id>/', views.criar_equipes, name='editar_equipes'),
    path('equipe/excluir/<int:id>/', views.excluir_equipes, name='excluir_equipes'),
    path('equipes/', views.listar_equipes, name='listar_equipes'),

    # urls para projetos
    path('projeto/criar', views.criar_projetos, name='criar_projetos'),
    path('projeto/alterar/<int:id>/', views.criar_projetos, name='editar_projetos'),
    path('projeto/excluir/<int:id>/', views.excluir_projetos, name='excluir_projetos'),
    path('projetos/', views.listar_projetos, name='listar_projetos'),

    # urls para tarefas
    path('tarefa/criar', views.criar_tarefas, name='criar_tarefas'),
    path('tarefa/alterar/<int:id>/', views.criar_tarefas, name='editar_tarefas'),
    path('tarefa/excluir/<int:id>/', views.excluir_tarefas, name='excluir_tarefas'),
    path('tarefas/', views.listar_tarefas, name='listar_tarefas'),
]