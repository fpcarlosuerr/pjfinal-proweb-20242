from django.db import models

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=400)
    CPF = models.CharField(max_length=14)
    email = models.EmailField()
    especialidade = models.CharField(max_length=200)

    def __str__(self):
        return Professor.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=400)
    carga_horaria = models.CharField(max_length=5)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return Disciplina.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=400)
    CPF = models.CharField(max_length=14)
    matricula = models.CharField(max_length=8)
    contato = models.CharField(max_length=11)
    disciplinas = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return Aluno.nome

class Nota(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nota = models.DecimalField(decimal_places=2, max_digits=4)

class Gerente(models.Model):
    nome = models.CharField(max_length=400)

    def __str__(self):
        return Gerente.nome