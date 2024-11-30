from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FuncionarioForm, SalaForm, EquipamentoForm, ReservaFom
from django.urls import reverse
from django.contrib import messages

def index_reuniao(request):
    return render(request, 'app_salas_reuniao/index_reuniao.html')

def cadastrar_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Funcionário cadastrado com sucesso")
            return HttpResponseRedirect(reverse('cadastrar_funcionario'))
    else:
        form = FuncionarioForm()
    return render(request, 'app_salas_reuniao/cadastrar_funcionario.html', {"form": form})

def cadastrar_sala(request):
    if request.method == "POST":
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect(reverse('cadastrar_sala'))
    else:
        form = SalaForm()
    return render(request, 'app_salas_reuniao/cadastrar_sala.html', {"form":form})

def cadastrar_equipamento(request):
    if request.method == "POST":
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cadastrar_equipamento'))
    else:
        form = EquipamentoForm()
    return render(request, 'app_salas_reuniao/_cadastrar_equipamento.html', {'form':form})

def resevar_sala(request):
    if request == "POST":
        form = ReservaFom(request.POST)
        if form.is_valid():
            form.save
            return HttpResponseRedirect(reverse('reservar_sala'))
    else:
        form = ReservaFom()
    return render(request, 'app_salas_reuniao/reservar_sala.html', {'form':form})