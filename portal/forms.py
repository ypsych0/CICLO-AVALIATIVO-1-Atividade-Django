from django import forms

# ERRO ENCONTRADO:'from models import Professor' procurava um módulo solto chamado 'models'. O models.py está dentro do app.
# CORRECAO: Então o import deve partir do pacote 'portal'. (LUCAS)

from portal.models import Professor


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro', 'disciplina',]