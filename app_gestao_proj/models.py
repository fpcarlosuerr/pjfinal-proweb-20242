from django.db import models
from django.core.exceptions import ValidationError

#Classe Membro 
class Membro(models.Model):  
    nome_membro = models.CharField(max_length = 200)
    funcao = models.TextField(null=True)
    email = models.EmailField(max_length=200, unique=True)
    telefone = models.CharField(max_length = 30, null= True, unique=True)
    equipe = models.ForeignKey(
        'Equipe',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        equipe_nome = self.equipe.nome_equipe if self.equipe else "Sem equipe"
        return f"{self.nome_membro} - {equipe_nome}"  # Ajuste 'equipe.nome' de acordo com o campo no modelo Equipe.

#Classe Equipe 
class Equipe(models.Model):
    nome_equipe = models.CharField(max_length=200, unique=True)
    descricao = models.TextField(null=True)

    def __str__(self):
        return self.nome_equipe

# Classe Projeto 
class Projeto(models.Model):
    situacao_choices = [
        (0, 'Não iniciada'),
        (1, 'Em andamento'),
        (2, 'Concluido'),
        (3, 'Abandonado')
    ]

    equipe_responsavel = models.OneToOneField(
        'Equipe',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    nome_projeto = models.CharField(max_length = 300)
    descricao = models.TextField(null= True)
    situacao = models.IntegerField(choices = situacao_choices) 
    data_inicio = models.DateField(null=True, blank=True)
    data_conclusao = models.DateField(null = True, blank=True)

    
    def __str__(self):
        return self.nome_projeto 

#Classe Tarefa 
class Tarefa(models.Model):
    situacao_choices = [
        (0, 'Não iniciada'),
        (1, 'Em andamento'),
        (2, 'Concluída'),
        (3, 'Abandonada')
    ]

    projeto = models.ForeignKey(
        'Projeto',
        on_delete=models.CASCADE,
    )
    nome_tarefa = models.CharField(max_length=200)
    descricao = models.TextField(null=True, blank=True)
    situacao = models.IntegerField(choices=situacao_choices)
    data_conclusao = models.DateField(null=True, blank=True)
    membros_equipe = models.ManyToManyField(
        'Membro',
        blank=True,  # Permite que uma tarefa seja criada sem membros inicialmente
    )

    def __str__(self):
        return self.nome_tarefa
        