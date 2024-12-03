from django import forms
from django.db import connection
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
               'nome': forms.TextInput(attrs={'class':'form-control'}),
               'CPF': forms.TextInput(attrs={'class':'form-control'}),
               'email': forms.EmailInput(attrs={'class':'form-control'}),
               'ramal': forms.TextInput(attrs={'class':'form-control'}),

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
          widgets = {
               'nome': forms.TextInput(attrs={'class':'form-control'}),
               'capacidade': forms.NumberInput(attrs={'class':'form-control'}),
               'localizacao': forms.TextInput(attrs={'class':'form-control'}),
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
               'nome': forms.TextInput(attrs={'class':'form-control'}),
               'sala': forms.Select(attrs={'class':'form-control'}),
          }
class ReservaForm(forms.ModelForm):
     class Meta:
          model = Reserva
          fields = ['funcionario','sala', 'data_horario_inicio', 'data_horario_termino', 'equipamento']

          labels = {
               'funcionario': "Selecione o funcionario:",
               'sala': "Selecione a sala:",
               'data_horario_inicio': "Data Inicio:",
               'data_horario_termino': "Data Fim:",
               'equipamento':" Selecione o Equipamento",
          }
          widgets = {
               'funcionario': forms.Select(attrs={'class':'form-control'}),
               'sala': forms.Select(attrs={'class':'form-control'}),
               'data_horario_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
               'data_horario_termino': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
          }
     def __init__(self, *args, **kwargs):
        sala_id = kwargs.pop('sala_id', None)  # Obtém o ID da sala se fornecido
        super(ReservaForm, self).__init__(*args, **kwargs)
        
        if sala_id:
            self.fields['equipamento'].queryset = Equipamento.objects.filter(sala_id=sala_id).order_by('nome')
        else:
            self.fields['equipamento'].queryset = Equipamento.objects.none()  # Se não houver sala, não mostra equipamentos
          