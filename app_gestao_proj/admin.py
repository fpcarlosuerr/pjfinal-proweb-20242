from django.contrib import admin
from .models import Membro, Equipe, Projeto

# Register your models here.
class MembroInline(admin.TabularInline):
    model = Equipe.membros_equipe.through  # Associa o campo ManyToMany
    extra = 1  # Número de linhas extras para novos membros

class EquipeAdmin(admin.ModelAdmin):
    inlines = [MembroInline]
    exclude = ('membros_equipe',)  # Evitar duplicação de campos

admin.site.register(Equipe, EquipeAdmin)