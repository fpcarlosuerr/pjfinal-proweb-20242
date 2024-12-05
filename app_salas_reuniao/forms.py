from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
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
               'equipamento': forms.CheckboxSelectMultiple(attrs={'class':'mb-3', 'id': 'id_equipamento'}),
          }

          def __init__(self, *args, **kwargs):
               super().__init__(*args, **kwargs)
               # Maneira de conseguirmos fazer surgir apenas as opções de equipamento de uma sala
               if 'sala' in self.data:
                    try:
                         sala_id = int(self.data.get('sala'))
                         self.fields['equipamento'].queryset = Equipamento.objects.filter(sala_id=sala_id).order_by('nome')
                    except (ValueError, TypeError):
                         pass
               elif self.instance.pk:  # Se for uma edição
                    self.fields['equipamentos'].queryset = self.instance.sala.equipamento_set.all()

               
     def clean(self):
          cleaned_data = super().clean()
          data_horario_inicio = cleaned_data.get('data_horario_inicio')
          data_horario_termino = cleaned_data.get('data_horario_termino')
          sala = cleaned_data.get('sala')

          # Verifica se ambos os horários foram preenchidos
          if data_horario_inicio and data_horario_termino:
               # Verifica se o horário de início é anterior ao horário de término
               if data_horario_inicio >= data_horario_termino:
                    raise ValidationError("A data/hora de início deve ser anterior à data/hora de término.")

               # Verifica se já existe uma reserva para a mesma sala no mesmo horário
               overlapping_reservas = Reserva.objects.filter(
                    sala=sala,
                    data_horario_inicio__lt=data_horario_termino,
                    data_horario_termino__gt=data_horario_inicio
               )
               if overlapping_reservas.exists():
                    raise ValidationError("Já existe uma reserva para esta sala nesse horário.")

               # Validação dos horários permitidos
               if not self.horarios_permitidos(data_horario_inicio) or not self.horarios_permitidos(data_horario_termino):
                    raise ValidationError("Os horários devem estar entre 08:00-12:00 ou 14:00-19:00.")

          return cleaned_data

     def horarios_permitidos(self, dt):
          """Verifica se o horário está dentro dos intervalos permitidos."""
          # Torna dt ciente do fuso horário, se for naive
          if timezone.is_aware(dt):
               dt = timezone.make_naive(dt)
          inicio_manha = timezone.datetime.combine(dt.date(), timezone.datetime.strptime("08:00", "%H:%M").time())
          fim_manha = timezone.datetime.combine(dt.date(), timezone.datetime.strptime("12:00", "%H:%M").time())
          inicio_tarde = timezone.datetime.combine(dt.date(), timezone.datetime.strptime("14:00", "%H:%M").time())
          fim_tarde = timezone.datetime.combine(dt.date(), timezone.datetime.strptime("19:00", "%H:%M").time())

          return (inicio_manha <= dt <= fim_manha) or (inicio_tarde <= dt <= fim_tarde)