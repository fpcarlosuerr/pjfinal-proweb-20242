from django.db import models

#Classe Membro 
class Membro(models.Model):  
    nome_membro = models.CharField(max_length = 200)
    funcao = models.TextField(null=True)
    email = models.EmailField(max_length=200, unique=True)
    telefone = models.CharField(max_length = 30, null= True)
    equipe = models.ForeignKey(
        'Equipe', 
        on_delete=models.SET_NULL,
        null=True,
        blank= True,
        related_name="membros"
    )

    
    def __str__(self):
        return self.nome_membro

#Classe Equipe 
class Equipe(models.Model):
    nome_equipe = models.CharField(max_length = 200, unique=True)
    membros_equipe = models.ManyToManyField(
        'Membro', related_name = "equipe_participam"
    )
    descricao = models.TextField(null= True)

    
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

    equipe_responsavel = models.ForeignKey(
        'Equipe',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    nome_projeto = models.CharField(max_length = 300, unique=True)
    descricao = models.TextField(null= True)
    situacao = models.IntegerField(choices = situacao_choices) 
    data_inicio = models.DateField()
    data_conclusao = models.DateField(null = True)

    
    def __str__(self):
        return self.nome_projeto 

#Classe Tarefa 
class Tarefa(models.Model):
    situacao_choices = [
        (0, 'Não iniciada'),
        (1, 'Em andamento'),
        (2, 'Concluida'),
        (3, 'Abandonada')
    ]

    projeto = models.ForeignKey(
       'Projeto', 
        related_name= "projeto",
        on_delete= models.CASCADE,
    )
    nome_tarefa = models.CharField(max_length = 200)
    descricao = models.TextField(null= True)
    situacao = models.IntegerField(choices = situacao_choices )
    data_conclusao = models.DateField(null= True)
    membros_tarefa = models.ManyToManyField(
        'Membro', related_name= "fazer_terefa",
    )

    def __str__(self):
        return self.nome_tarefa