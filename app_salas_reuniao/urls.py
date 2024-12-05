from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_reuniao, name='index_reuniao'),

    # Urls de funcionario
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('alterar_funcionairio/<int:id>/', views.cadastrar_funcionario, name='alterar_funcionario'),
    path('excluir_funcionario/<int:id>/', views.excluir_funcionario, name='excluir_funcionario'),
    path('funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),

    # Urls de sala
    path('cadastrar_sala/', views.cadastrar_sala, name='cadastrar_sala'),
    path('alterar_sala/<int:id>/', views.cadastrar_sala, name='alterar_sala'),
    path('excluir_sala/<int:id>/', views.excluir_sala, name='excluir_sala'),
    path('salas/', views.listar_sala, name='listar_sala'),

    # Urls de reserva sala de reunião
    path('resevar_sala/', views.resevar_sala, name='resevar_sala'),
    path('alterar_reserva/<int:id>/', views.resevar_sala, name='alterar_reserva'),
    path('excluir_reserva/<int:id>/', views.excluir_reserva, name='excluir_reserva'),
    path('atualizar_equipamento', views.atualizar_equipamento, name='atualizar_equipamento'),

    # Urls de Equipamento
    path('cadastrar_equipamento/', views.cadastrar_equipamento, name='cadastrar_equipamento'),
    path('alterar_equipamento/<int:id>/', views.cadastrar_equipamento, name='alterar_equipamento'),
    path('excluir_equipamento/<int:id>/', views.excluir_equipamento, name='excluir_equipamento'),
    path('equipamentos/', views.listar_equipamentos, name='listar_equipamentos'),
]