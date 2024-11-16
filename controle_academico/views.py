from django.shortcuts import render

# Create your views here.

def index_controle_academico(request):
    return render(request, 'controle_academico/index_controle_academico.html')