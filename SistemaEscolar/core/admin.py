from django.contrib import admin
from .models import Turma, Aluno

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'professor')
    search_fields = ('nome', 'professor__username')
    list_filter = ('professor',)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turma', 'nota_media')
    search_fields = ('nome', 'turma__nome')
    list_filter = ('turma',)
