from django.contrib import admin
from portal import models

@admin.register(models.Professor)
class ProfessorAdmin(admin.ModelAdmin):
    
    # ERRO ENCONTRADO:'especialidade' não existe no model Professor;
    #  CORRECAO: O campo se chama 'disciplina' (SAMUEL)

    list_display = ('id', 'nome', 'email', 'telefone', 'disciplina', 'ativo',)

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno_id', 'professor_id', 'status',)
