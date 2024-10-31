from django.shortcuts import render

# Create your views here.
def index_applocaimoveis(request):
    
    return render(request,'applocaimoveis/index_applocaimoveis.html')