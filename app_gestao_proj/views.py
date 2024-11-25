from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Membro, Equipe, Tarefa, Projeto
from .forms import MembroForm

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