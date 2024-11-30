from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Membro, Equipe, Tarefa, Projeto
from .forms import MembroForm, EquipeForm, ProjetoForm, TarefaForm


# Create your views here.

# Metodo para a página de login
def app_gestao_proj(request):
    
    return render(request,'app_gestao_proj/base_app_gestao.html')

# Metodo para casdastro de membros do projeto
def cadastrar_membros(request, id=None):
    membro = get_object_or_404(Membro, pk=id) if id else None
    lista_membros = Membro.objects.all()

    if request.method == "POST":
        form = MembroForm(request.POST, instance=membro)
        if form.is_valid():
            form.save()
            if membro:
                messages.success(request, 'Cadastro atualizado com sucesso!')
            else:
                messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('listar_membros')
        else:
            messages.error(request, 'Erro ao atualizar membro!!')
    else:
        form = MembroForm(instance=membro)
    
    return render(request, 'app_gestao_proj/forms_membro.html', {
        'form': form,
        'lista_membros': lista_membros,
        'membro': membro
    })

#Metodo para listar os membros cadastrados
def listar_membros(request):
    membro = None
    lista_membros = Membro.objects.all()
    form = MembroForm(instance=membro)
    return render(request, 'app_gestao_proj/forms_membro.html', {
        'form': form,
        'lista_membros': lista_membros,
        'membro': membro
    })

# Método para excluir o cadastro de uma pessoa
def excluir_membros(request, id):
    membro = get_object_or_404(Membro,pk=id)
    membro.delete()
    membro = None
    lista_membros = Membro.objects.all()
    form = MembroForm(instance = membro )
    return render(request, 'app_gestao_proj/forms_membro.html', {
        'form': form,
        'lista_membros': lista_membros,
        'membro': membro
    })

# Método para o cadastro de equipes
def criar_equipes(request, id = None):
    equipe = get_object_or_404(Equipe, pk=id) if id else None
    lista_equipes = Equipe.objects.all()

    if request.method == "POST":
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            form.save()
            if equipe:
                messages.success(request, 'Cadastro atualizado com sucesso!')
            else:
                messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('listar_equipes')
        else:
            messages.error(request, 'Erro ao atualizar Equipe!!')
    else:
        form = EquipeForm(instance=equipe)
    
    return render(request, 'app_gestao_proj/forms_equipe.html', {
        'form': form,
        'lista_equipes': lista_equipes,
        'equipe': equipe
    })

# Método para listar as equipes
def listar_equipes(request):
    equipe = None
    lista_equipes = Equipe.objects.all()
    form = EquipeForm(instance=equipe)
    return render(request, 'app_gestao_proj/forms_equipe.html', {
        'form': form,
        'lista_equipes': lista_equipes,
        'equipe': equipe
    })

# Método para excluir o cadastro de uma pessoa
def excluir_equipes(request, id):
    equipe = get_object_or_404(Equipe,pk=id)
    equipe.delete()
    equipe = None
    lista_equipes = Equipe.objects.all()
    form = EquipeForm(instance = equipe )
    return render(request, 'app_gestao_proj/forms_equipe.html', {
        'form': form,
        'lista_equipes': lista_equipes,
        'equipe': equipe
    })

# Método para o cadastro de Projetos 
def criar_projetos(request, id = None):
    projeto = get_object_or_404(Projeto, pk=id) if id else None
    lista_projetos = Projeto.objects.all()

    if request.method == "POST":
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            if projeto:
                messages.success(request, 'Cadastro atualizado com sucesso!')
            else:
                messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('listar_projetos')
        else:
            messages.error(request, 'Erro ao atualizar Projeto!!')
    else:
        form = ProjetoForm(instance=projeto)
    
    return render(request, 'app_gestao_proj/forms_projeto.html', {
        'form': form,
        'lista_projetos': lista_projetos,
        'projeto': projeto
    })

# Método para listar as projetos
def listar_projetos(request):
    projeto = None
    lista_projetos = Projeto.objects.all()
    form = ProjetoForm(instance=projeto)
    return render(request, 'app_gestao_proj/forms_projeto.html', {
        'form': form,
        'lista_projetos': lista_projetos,
        'projeto': projeto
    })

# Método para excluir o cadastro de uma pessoa
def excluir_projetos(request, id):
    projeto = get_object_or_404(Projeto,pk=id)
    projeto.delete()
    projeto = None
    lista_projetos = Projeto.objects.all()
    form = ProjetoForm(instance = projeto )
    return render(request, 'app_gestao_proj/forms_projeto.html', {
        'form': form,
        'lista_projetos': lista_projetos,
        'projeto': projeto
    })

# Método para o cadastro de Tarefas 
def criar_tarefas(request, id=None):
    tarefa = get_object_or_404(Tarefa, pk=id) if id else None
    lista_tarefas = Tarefa.objects.all()

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            if tarefa:
                messages.success(request, 'Tarefa atualiazada com sucesso!')
            else:
                messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('listar_tarefas')
        else:
            messages.error(request, 'Erro ao atualizar tarefa!!')
    else:
        form = TarefaForm(instance=tarefa)
    
    return render(request, 'app_gestao_proj/forms_tarefa.html', {
        'form':form,
        'lista_tarefas':lista_tarefas,
        'tarefa': tarefa
    })

# Método para listar tarefas 
def listar_tarefas(request):
    tarefa = None
    lista_tarefas = Tarefa.objects.all()
    form = TarefaForm(instance=tarefa)
    return render(request, 'app_gestao_proj/forms_tarefa.html', {
        'form':form,
        'lista_tarefas':lista_tarefas,
        'tarefa':tarefa,
    })

# Método para excluir tarefas 
def excluir_tarefas(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    tarefa.delete()
    tarefa = None
    lista_tarefas = Tarefa.objects.all()
    form = TarefaForm(instance=tarefa)
    return render(request, 'app_gestao_proj/forms_tarefa.html',{
        'form':form,
        'lista_tarefas':lista_tarefas,
        'tarefa':tarefa,
    })

    

