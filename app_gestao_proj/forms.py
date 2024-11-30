from django import forms
from .models import Membro, Equipe, Tarefa, Projeto

class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ['nome_membro', 'funcao', 'email', 'telefone', 'equipe']
        labels = {
            'nome_membro':'Nome',
            'funcao':'Função', 
            'email':'E-mail',
            'telefone':'Telefone',
            'equipe':'Equipe'
        }
        widgets = {
            'nome_membro':forms.TextInput(attrs={'class':'form-control'}),
            'funcao': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'forms-control', 'type':'email'}),
            'telefone': forms.TextInput(attrs={'class':'form-control'}),
            'equipe': forms.Select(attrs={'class':'form-control'})
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Adiciona uma opção vazia ao campo equipe_responsavel
            self.fields['equipe'].empty_label = "Nenhuma equipe selecionada"

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['equipe_responsavel','nome_projeto', 'descricao', 'situacao', 'data_inicio', 'data_conclusao']
        labels = {
            'equipe_responsavel':'Equipe responsavel',
            'nome_projeto':'Nome do Projeto',
            'descricao':'Descrição',
            'situacao': 'Situação',
            'data_inicio':'Data de Inicio',
            'data_conclusao': 'Data de Conclusão',
        }
        widgets = {
            'equipe_responsavel':forms.Select(attrs={'class':'form-control'}),
            'nome_projeto':forms.TextInput(attrs={'class':'form-control'}),
            'descricao':forms.TextInput(attrs={'class':'form-control'}), 
            'situacao':forms.Select(attrs={'class':'form-control', 'type':'number'}),
            'data_inicio':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'data_conclusao':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona uma opção vazia ao campo equipe_responsavel
        self.fields['equipe_responsavel'].empty_label = "Nenhuma equipe selecionada"

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
            'membros_equipe':forms.SelectMultiple(attrs={'class':'form-control','multiple': True}),
            'descricao':forms.TextInput(attrs={'class':'form-control'}),
        }

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['equipe_responsavel', 'nome_projeto', 'descricao', 'situacao', 'data_inicio', 'data_conclusao']
        labels = {
            'equipe_responsavel':'Equipe Responsavel',
            'nome_projeto':'Nome do Projeto',
            'descricao':'Descricão',
            'situacao':'Situação', 
            'data_inicio':'Data de Inicio', 
            'data_conclusao':'Data de Conclusão',
        }
        widgets = {
            'equipe_responsavel':forms.Select(attrs={'class':'form-control'}),
            'nome_projeto':forms.TextInput(attrs={'class':'form-control'}),
            'descricao':forms.TextInput(attrs={'class':'form-control'}),
            'situacao':forms.Select(attrs={'class':'form-control'}),
            'data_inicio':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'data_conclusao':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['projeto', 'nome_tarefa', 'descricao', 'situacao', 'data_conclusao', 'membros_tarefa']
        labels = {
            'projeto':'Projeto',
            'nome_tarefa':'Tarefa',
            'descricao':'Descrição',
            'situacao':'Situação',
            'data_conclusao':'Data de Conclusão',
            'membros_tarefa':'Membros',
        }
        widgets = {
            'projeto':forms.Select(attrs={'class':'form-control'}),
            'nome_tarefa':forms.TextInput(attrs={'class':'form-control'}),
            'descricao':forms.TextInput(attrs={'class':'form-control'}),
            'situacao':forms.Select(attrs={'class':'form-control'}),
            'data_conclusao':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'membros_tarefa':forms.Select(attrs={'class':'form-control'}),
        }