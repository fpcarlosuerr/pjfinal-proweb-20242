from django import forms
from .models import Funcionario, Sala, Equipamento, Reserva

class FuncionarioForm(forms.ModelForm):
     class Meta:
          model = Funcionario
          fields = ['nome','CPF','email','ramal']

          labels = {
               'nome': "Nome",
               'CPF': "CPF",
               'email': "E-mail",
               'ramal': "Ramal"
          }
          widgets = {
               'ramal': forms.NumberInput()
          }

class SalaForm(forms.ModelForm):
     class Meta:
          model = Sala
          fields = ['nome','capacidade','localizacao']

          labels = {
               'nome': "Nome",
               'capacidade': "Capacidade",
               'localizacao': "Localização",
          }

class EquipamentoForm(forms.ModelForm):
     class Meta:
          model = Equipamento
          fields = ['sala','nome']

          labels = {
               'nome': "Nome:",
               'sala': "Sala:",
          }
          widgets = {
               "sala": forms.Select(attrs={'classe': 'form-control'})
          }

class ReservaFom(forms.ModelForm):
     class Meta:
          model = Reserva
          fields = ['funcionario','sala', 'data_horario_inicio', 'data_horario_termino', 'equipamento']

          labels = {
               'funcionario': "Selecione o funcionario:",
               'sala': "Selecione a sala:",
               'data_horario_inicio': "Data:",
               'data_horario_termino': "Data:",
               'equipamento':" Selecione o Equipamento",
          }
          