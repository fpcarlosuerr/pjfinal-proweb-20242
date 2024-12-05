from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from .forms import FuncionarioForm, SalaForm, EquipamentoForm, ReservaForm
from django.urls import reverse
from django.contrib import messages
from .models import Reserva, Equipamento, Sala, Funcionario


def index_reuniao(request):
    reservas = Reserva.objects.all()
    return render(request, 'app_salas_reuniao/index_reuniao.html', {
        'reservas': reservas,
    })

def cadastrar_funcionario(request, id=None):
    funcionario = get_object_or_404(Funcionario, pk=id) if id else None
    lista_funcionarios = Funcionario.objects.all()
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            if funcionario:
                messages.success(request, "Funcionário alterado com sucesso")
            else:
                messages.success(request, "Funcionário cadastrado com sucesso")
            return redirect('listar_funcionarios')
        else:
            messages.error(request, f'Erro ao atualizar Funcionario: {funcionario.nome}')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'app_salas_reuniao/cadastrar_funcionario.html', {
        'form': form,
        'lista_funcionarios':lista_funcionarios,
        'funcionario': funcionario
    })

def listar_funcionarios(request):
    funcionario = None
    lista_funcionarios = Funcionario.objects.all()
    form = FuncionarioForm(instance=funcionario)
    print('cheguei aqui',lista_funcionarios)
    return render(request, 'app_salas_reuniao/cadastrar_funcionario.html', {
        'form': form,
        'lista_funcionarios':lista_funcionarios,
        'funcionario': funcionario
    })

def excluir_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario,pk=id)
    funcionario.delete()
    funcionario = None
    lista_funcionarios = Funcionario.objects.all()
    form = FuncionarioForm(instance = funcionario )
    return render(request, 'app_salas_reuniao/cadastrar_funcionario.html', {
        'form': form,
        'lista_funcionarios':lista_funcionarios,
        'funcionario': funcionario
    })

def cadastrar_sala(request, id=None):
    sala = get_object_or_404(Sala, pk=id) if id else None
    lista_salas = Sala.objects.all()

    if request.method == "POST":
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save() 
            if sala:
                messages.success(request, 'Sala atualizada')
            else:
                messages.success(request, "Sala cadastrada com sucesso")
            return redirect('listar_sala')
        else:
            messages.error(request, 'Erroa ao atualizar Equipe')
    else:
        form = SalaForm(instance=sala)
        
    return render(request, 'app_salas_reuniao/cadastrar_sala.html', {
        'form':form, 
        'lista_salas':lista_salas, 
        'sala': sala
    })

# metodo para listar salas cadastradas
def listar_sala(request):
    sala = None
    lista_salas = Sala.objects.all()
    form = SalaForm(instance=sala)
    return render(request, 'app_salas_reuniao/cadastrar_sala.html', {
        'form': form,
        'lista_salas': lista_salas,
        'sala': sala
    })

# Método para excluir sala
def excluir_sala(request, id):
    sala = get_object_or_404(Sala,pk=id)
    sala.delete()
    sala = None
    lista_salas = Sala.objects.all()
    form = SalaForm(instance = sala )
    return render(request, 'app_salas_reuniao/cadastrar_sala.html', {
        'form': form,
        'lista_salas': lista_salas,
        'sala': sala
    })

def cadastrar_equipamento(request, id=None):
    equipamento = get_object_or_404(Equipamento, pk=id) if id else None
    lista_equipamentos = Equipamento.objects.all()

    if request.method == "POST":
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            if equipamento:
                messages.success(request, 'Equipamento atualizado')
            else:
                messages.success(request, "Equipamento cadastrado com sucesso")
            return redirect('listar_equipamentos')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'app_salas_reuniao/_cadastrar_equipamento.html', {
        'form':form,
        'lista_equipamentos':lista_equipamentos, 
        'equipamento': equipamento
    })

def listar_equipamentos(request):
    equipamento = None
    lista_equipamentos = Equipamento.objects.all()
    form = EquipamentoForm(instance=equipamento)
    return render(request, 'app_salas_reuniao/_cadastrar_equipamento.html', {
        'form': form,
        'lista_equipamentos': lista_equipamentos,
        'equipamento': equipamento
    })


def excluir_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento,pk=id)
    equipamento.delete()
    equipamento = None
    lista_equipamentos = Equipamento.objects.all()
    form = EquipamentoForm(instance = equipamento )
    return render(request, 'app_salas_reuniao/_cadastrar_equipamento.html', {
        'form': form,
        'lista_equipamentos': lista_equipamentos,
        'equipamento': equipamento
    })

def resevar_sala(request, id=None):
    reserva = get_object_or_404(Reserva, pk=id) if id else None

    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            try:
                form.save()
                if reserva:
                    messages.success(request, 'Reserva atualizada')
                else:
                    messages.success(request, "Reserva cadastrado com sucesso")
                return redirect('resevar_sala')
            except ValidationError as e:
                messages.error(request, e)
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'app_salas_reuniao/reservar_sala.html', {'form':form, 'reserva':reserva})

def excluir_reserva(request, id):
    reserva = get_object_or_404(Reserva,pk=id)
    reserva.delete()
    reservas = Reserva.objects.all()
    reserva = None
    form = EquipamentoForm(instance = reserva )
    return render(request, 'app_salas_reuniao/index_reuniao.html', {
        'form': form,
        'reserva': reserva,
        'reservas': reservas
    })

def atualizar_equipamento(request):
    sala_id = request.GET.get('sala_id')
    equipamentos = Equipamento.objects.filter(sala_id=sala_id).values('id', 'nome')
    return JsonResponse(equipamentos, safe=False)
