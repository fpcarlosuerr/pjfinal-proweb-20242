from django.db import models

#Classe Membro 
class Membro(models.Model):  
    nome_membro = models.CharField(max_length = 200)
    funcao = models.TextField(null=True)
    email = models.EmailField(max_length=200, unique=True)
    telefone = models.CharField(max_length = 30, null= True)

    
    def __str__(self):
        return self.nome_membro

#Classe Equipe 
class Equipe(models.Model):
    nome_equipe = models.CharField(max_length = 200)
    membros_equipe = models.ManyToManyField(
        Membro, related_name = "equipe_participam"
    )
    descricao = models.TextField(null= True)

    
    def __str__(self):
        return self.nome_equipe

# Classe Projeto 
class Projeto(models.Model):
    situacao_choices = [
        (1, 'Iniciado'),
        (2, 'Concluido'),
        (3, 'Abandonado')
    ]
    nome_proj = models.CharField(max_length = 300)
    descricao = models.TextField(null= True)
    situacao = models.IntegerField(choices = situacao_choices) 
    data_inicio = models.DateTimeField()
    data_conclusao = models.DateTimeField(null = True)

    
    def __str__(self):
        return self.nome_proj

#Classe Tarefa 
class Tarefa(models.Model):
    situacao_choices = [
        (1, 'Iniciada'),
        (2, 'Concluida'),
        (3, 'Abandonada')
    ]

    nome_tarefa = models.CharField(max_length = 200)
    descricao = models.TextField(null= True)
    situacao = models.IntegerField(choices = situacao_choices )
    data_conclusao = models.DateField(null= True)
    equipe_responsavel = models.ForeignKey(
        Equipe, 
        on_delete = models.SET_NULL,
        null=True,
        related_name= "tarefa_responsavel"
    )
    membros_tarefa = models.ManyToManyField(
        Membro, related_name= "fazer_terefa",
    )
    projeto = models.ForeignKey(
        Projeto, 
        related_name= "projeto",
        on_delete= models.CASCADE,
    )

    def __str__(self):
        return self.nome_tarefa