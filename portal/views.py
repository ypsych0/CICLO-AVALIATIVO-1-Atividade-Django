from django.shortcuts import render
from portal.forms import ProfessorForm


def index(request):

    # ERRO ENCONTRADO: o caminho era 'templates/portal/index.html'. O Django já procura dentro da pasta templates/ de cada app, então o caminho começa em 'portal/'.
    # CORRECAO: Mudei para 'portal/index.html' (PEDRO)
    return render(

        request,
        'portal/index.html'
    )


# ERRO ENCONTRADO:o portal/urls.py apontava para views.cadastro, mas essa view não existia (AttributeError). Foi criada aqui para renderizar o cadastro.html.
# CORRECAO: Criei a view cadastro() (PEDRO)
def cadastro(request):
    salvo = False
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProfessorForm()
            salvo = True
    else:
        form = ProfessorForm()
    return render(request, 'portal/cadastro.html', {'form': form, 'salvo': salvo})
