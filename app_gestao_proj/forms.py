from django import forms
from .models import Membro, Equipe, Tarefa, Projeto

class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ['nome_membro', 'funcao', 'email', 'telefone']
        labels = {
            'nome_membro':'Nome',
            'funcao':'Função', 
            'email':'E-mail',
            'telefone':'Telefone',
        }
        widgets = {
            'nome_membro':forms.TextInput(attrs={'class':'form-control'}),
            'funcao': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'forms-control', 'type':'email'}),
            'telefone': forms.TextInput(attrs={'class':'form-control'}),
        }

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome_projeto', 'descricao', 'situacao', 'data_inicio', 'data_conclusao']
        labels = {
            'nome_projeto':'Nome do Projeto',
            'descricao':'Descrição',
            'situacao': 'Situação',
            'data_inicio':'Data de Inicio',
            'data_conclusao': 'Data de Conclusão',
        }
        widgets = {
            'nome_projeto':forms.TextInput(attrs={'class':'form-control'}),
            'descricao':forms.TextInput(attrs={'class':'form-control'}), 
            'situacao':forms.Select(attrs={'class':'form-control', 'type':'number'}),
            'data_inicio':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'data_conclusao':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
        }

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome_equipe', 'membros_equipe', 'descricao']
        labels = {
            'nome_equipe':'Nome da Equipe',
            'membros_equipe':'Membros da Equipe',
            'descricao':'Descrição',
        }
        widgets = {
            'nome_equipe':forms.TextInput(attrs={'class':'form-control'}),
            'membros_equipe':forms.Select(attrs={'class':'form-control'}),
            'descricao':forms.TextInput(attrs={'class':'form-control'}),
        }

# class TarefaForm(forms.ModelForm):
#     class Meta:
#         model = Tarefa
#         fields = ['projeto','nome_tarefa', 'descricao', 'equipe_responsavel', 'situacao', '']