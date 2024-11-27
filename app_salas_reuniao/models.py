from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=400)
    CPF = models.CharField(max_length=14)
    email = models.EmailField()
    ramal = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return self.nome

class Sala(models.Model):
    nome = models.CharField(max_length=400)
    capacidade = models.IntegerField()
    localizacao = models.CharField(max_length=500)

    def __str__(self):
        return self.nome
    
class Equipamento(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, default=1)
    nome = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, default=1)
    data_horario_inicio = models.DateTimeField()
    data_horario_termino = models.DateTimeField()

    def __str__(self):
        return 'Sala: {sala} reservada para {funcionario} de {data_horario_inicio} até {data_horario_termino}'
    