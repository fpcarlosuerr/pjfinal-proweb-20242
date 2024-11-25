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

