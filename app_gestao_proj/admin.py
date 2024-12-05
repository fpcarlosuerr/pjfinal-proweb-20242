from django.contrib import admin
from .models import Membro, Equipe, Projeto

admin.site.register(Equipe)
admin.site.register(Membro)
admin.site.register(Projeto)