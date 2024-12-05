from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Prefetch
from django.db.models import F, Q, Case, When, IntegerField, Count #
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

    #Instacia os objetos presentes em equipe
    equipes = Equipe.objects.all()
    # Verifica se existem equipes no banco de dados
    if not equipes.exists():
        return render(request, 'app_gestao_proj/forms_membro.html', {
            'message': 'Nenhuma equipe encontrada. Por favor, cadastre uma equipe antes de adicionar membros.',
            'equipe_form_url': 'criar_equipes',  # Nome da URL para cadastro de equipes
        })
    
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
def criar_equipes(request, id=None):
    # Busca a equipe pelo ID ou define como None se for um novo cadastro
    equipe = get_object_or_404(Equipe, pk=id) if id else None
    lista_equipes = Equipe.objects.all()

    if request.method == "POST":
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            equipe_salva = form.save()  # Salva a equipe e associa os membros
            if equipe:
                messages.success(request, 'Cadastro atualizado com sucesso!')
            else:
                messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('listar_equipes')
        else:
            messages.error(request, 'Erro ao salvar a equipe! Verifique os dados informados.')
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

def criar_tarefas(request, id=None):
    # Obter a tarefa se o ID for fornecido, caso contrário, cria uma nova tarefa
    tarefa = get_object_or_404(Tarefa, pk=id) if id else None
    lista_tarefas = Tarefa.objects.all()

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            tarefa = form.save(commit=False)
            projeto = tarefa.projeto
            print("Projeto associado à tarefa:", projeto)

            # Validar os membros da tarefa com base na equipe do projeto
            if projeto:
                if not projeto.equipe_responsavel:
                    messages.error(request, 'Equipe responsavel não definida pelo projeto. Verifique o cadstro do projeto.')
                else:
                    equipe_membros = projeto.equipe_responsavel.membro_set.all()
                    membros_selecionados = form.cleaned_data.get('membros_equipe')
                    
                    if not membros_selecionados:
                        messages.error(request, 'Nenhum membro foi selecionado no formulário! Selecione pelo menos um membro da equipe resposável.')
                    else:
                        # Verifica se os membros selecionados pertencem à equipe do projeto
                        if not set(membros_selecionados).issubset(set(equipe_membros)):
                            messages.error(request, 'Nem todos os membros pertencem à equipe responsável pelo projeto! Verifique os dados inseridos.')
                            return render(request, 'app_gestao_proj/forms_tarefa.html', {
                                'form': form,
                                'lista_tarefas': lista_tarefas,
                                'tarefa': tarefa
                            })
            else:
                messages.error(request, 'Projeto não associado a tareta! Selecione um projeto.')

            tarefa.save()
            form.save_m2m()  # Salvar os membros relacionados no campo manytomany
            # Salvando a tarefa e os membros

            # Verificando se os membros foram salvos corretamente
            tarefa.refresh_from_db()  # Atualiza a instância da tarefa do banco de dados

            # Mensagem de sucesso
            if id:
                messages.success(request, 'Tarefa atualizada com sucesso!')
            else:
                messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('listar_tarefas')
        
        else:
            messages.error(request, 'Erro ao salvar a tarefa! Verifique os dados inseridos.')
    else:
        form = TarefaForm(instance=tarefa)
    
    return render(request, 'app_gestao_proj/forms_tarefa.html', {
        'form': form,
        'lista_tarefas': lista_tarefas,
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

# Calcula o progresso de cada projeto
def progresso_projetos(request):
#Código experimental------------------------------------------
    # Modelo do formulário de tarefas apenas para 'situacao'
    TarefaForm = modelform_factory(
        Tarefa,
        fields=['situacao'],  # Apenas o campo 'situacao' será editável
    )

    if request.method == 'POST':
        tarefa_id = request.POST.get('tarefa_id')
        tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
        form = TarefaForm(request.POST, instance=tarefa)

        if form.is_valid():
            tarefa = form.save()
            messages.success(request, 'Situação da tarefa atualizada com sucesso!')
            return redirect('base_app_gestao')
        else:
            messages.error(request, 'Erro ao atualizar a situação da tarefa.')

#Código experimental------------------------------------------
    # Anotações para calcular tarefas concluídas e progresso
    projetos = Projeto.objects.annotate(
        total_tarefas=Count('tarefa'),
        tarefas_concluidas=Count('tarefa', filter=Q(tarefa__situacao=2)),  # 2 = 'Concluída'
        progresso=Case(
            When(total_tarefas=0, then=0),  # Evita divisão por zero
            default=(F('tarefas_concluidas') * 100) / F('total_tarefas'),
            output_field=IntegerField()
        )
    )
    # Pré-carrega tarefas e membros para evitar consultas extras
    projetos = projetos.prefetch_related(
        Prefetch(
            'tarefa_set',  # Nome da relação reversa do `ForeignKey` em Tarefa para Projeto
            queryset=Tarefa.objects.prefetch_related('membros_equipe')  # Pré-carrega membros associados
        )
    )
    # Passar as escolhas de situação para o contexto
    situacao_choices = Tarefa.situacao_choices
    return render(request, 'app_gestao_proj/base_app_gestao.html', {
        'projetos': projetos,
        'situacao_choices': situacao_choices,
    })
