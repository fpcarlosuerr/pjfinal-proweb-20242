from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from .forms import FuncionarioForm, SalaForm, EquipamentoForm, ReservaForm
from django.urls import reverse
from django.contrib import messages
from .models import Reserva, Equipamento


def index_reuniao(request):
    reservas = Reserva.objects.all()
    return render(request, 'app_salas_reuniao/index_reuniao.html', {'reservas': reservas})

def cadastrar_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Funcionário cadastrado com sucesso")
            return HttpResponseRedirect(reverse('cadastrar_funcionario'))
    else:
        form = FuncionarioForm()
    return render(request, 'app_salas_reuniao/cadastrar_funcionario.html', {'form': form})

def cadastrar_sala(request):
    if request.method == "POST":
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "Sala cadastrada com sucesso")
            return HttpResponseRedirect(reverse('cadastrar_sala'))
    else:
        form = SalaForm()
    return render(request, 'app_salas_reuniao/cadastrar_sala.html', {'form':form})

def cadastrar_equipamento(request):
    if request.method == "POST":
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Equipamento cadastrado com sucesso")
            return HttpResponseRedirect(reverse('cadastrar_equipamento'))
    else:
        form = EquipamentoForm()
    return render(request, 'app_salas_reuniao/_cadastrar_equipamento.html', {'form':form})

def resevar_sala(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Reservar feita com sucesso!!!")
                return HttpResponseRedirect(reverse('resevar_sala'))
            except ValidationError as e:
                messages.error(request, e)
        else:
            messages.error(request, 'RESERVA NÃO REALIZADA!!!')
    else:
        form = ReservaForm()
    return render(request, 'app_salas_reuniao/reservar_sala.html', {'form':form})

def get_equipamentos(request, sala_id):
    equipamentos = Equipamento.objects.filter(sala_id=sala_id).values('id', 'nome')
<<<<<<< HEAD
    return JsonResponse(equipamentos, safe=False)
=======
    return JsonResponse({'equipamentos': list(equipamentos)})
>>>>>>> parent of 54cbfac (Componete equipamento cadastrado com base na sala, equipe 4)
