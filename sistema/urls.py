from django.contrib import admin
from django.urls import path, include  # ERRO ENCONTRADO: estava faltando o include() para delegar as rotas do app portal.
                                       # CORRECAO: Adicionei o include() (LUCAS)

urlpatterns = [
    path('admin/', admin.site.urls),

    # ERRO ENCONTRADO: no segundo argumento do path() havia uma frase solta ("preciso mostrar a página
    # cadastro.html"), o que causa SyntaxError. O urls.py global deve delegar as rotas do app ao portal/urls.py usando include().
    # CORRECAO: Adicionei include('portal.urls') (SAMUEL)

    path('', include('portal.urls')),
]
