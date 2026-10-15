# CICLO-AVALIATIVO-1-Atividade-Django

# Sistema Escolar Django — Projeto Corrigido

Projeto Django de um sistema escolar com cadastro de **Professores**, **Alunos** e **Aulas**.
Este repositório contém a versão **corrigida** do projeto base
[`Will-firmino/sistema_escolar_django`](https://github.com/Will-firmino/sistema_escolar_django),
que tinha erros propositais de código e configuração.

## Tecnologias

- Python 3
- Django
- SQLite
- Pillow (necessário por causa dos `ImageField`)

## Como rodar

```bash
git clone <URL-DO-SEU-REPOSITORIO>
cd sistema_escolar_django

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install django pillow

python manage.py migrate
python manage.py runserver
```

Rotas disponíveis:

| Rota         | Descrição                       |
|--------------|---------------------------------|
| `/index/`    | Página inicial do portal        |
| `/cadastro/` | Formulário de cadastro de professor |
| `/admin/`    | Painel administrativo           |

## Estrutura

```
sistema_escolar_django/
├── manage.py
├── sistema/          # configurações do projeto (settings, urls)
└── portal/           # app principal (models, views, forms, admin, templates)
```

## Erros encontrados e correções

Foram encontrados **8 erros**. Cada um está comentado no código com `# ERRO:`
logo acima da linha corrigida.

### 1. App `portal` não registrado — `sistema/settings.py`
- **Erro:** o app não estava em `INSTALLED_APPS`.
- **Sintoma:** o Django não reconhece os models, templates e migrations do app (`RuntimeError` sobre `app_label`).
- **Correção:** adicionar `'portal'` à lista `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    ...
    'portal',
]
```

### 2. `include` não importado — `sistema/urls.py`
- **Erro:** faltava importar `include` para delegar as rotas do app `portal`.
- **Sintoma:** `NameError: name 'include' is not defined`.
- **Correção:**

```python
from django.urls import path, include
```

### 3. Frase solta no `path()` — `sistema/urls.py`
- **Erro:** no segundo argumento do `path()` havia uma frase solta (`preciso mostrar a página cadastro.html`).
- **Sintoma:** `SyntaxError` ao iniciar o servidor.
- **Correção:** o `urls.py` global deve delegar as rotas ao `portal/urls.py` usando `include()`.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portal.urls')),
]
```

### 4. `timezone` não importado — `portal/models.py`
- **Erro:** `default=timezone.now` era usado em `Professor`, `Aluno` e `Aula` sem o import.
- **Sintoma:** `NameError: name 'timezone' is not defined`.
- **Correção:**

```python
from django.utils import timezone
```

### 5. Import incorreto — `portal/forms.py`
- **Erro:** `from models import Professor` procurava um módulo solto chamado `models`.
- **Sintoma:** `ModuleNotFoundError`.
- **Correção:** o import deve partir do pacote do app.

```python
from portal.models import Professor
```

### 6. Campo inexistente no admin — `portal/admin.py`
- **Erro:** `list_display` do `ProfessorAdmin` usava `'especialidade'`, que não existe no model.
- **Sintoma:** erro de sistema (`admin.E108`) ao rodar o projeto.
- **Correção:** usar o nome real do campo, `'disciplina'`.

```python
list_display = ('id', 'nome', 'email', 'telefone', 'disciplina', 'ativo',)
```

### 7. Caminho errado do template — `portal/views.py`
- **Erro:** o `render` usava `'templates/portal/index.html'`.
- **Sintoma:** `TemplateDoesNotExist`.
- **Correção:** o Django já procura dentro da pasta `templates/` de cada app, então o caminho começa em `portal/`.

```python
return render(request, 'portal/index.html')
```

### 8. View `cadastro` inexistente — `portal/views.py`
- **Erro:** `portal/urls.py` apontava para `views.cadastro`, mas a função não existia.
- **Sintoma:** `AttributeError: module 'portal.views' has no attribute 'cadastro'`.
- **Correção:** criar a view que renderiza o `cadastro.html` com o formulário.

```python
def cadastro(request):
    form = ProfessorForm()
    return render(request, 'portal/cadastro.html', {'form': form})
```

## Resultado

Após as correções:

- `python manage.py check` → *System check identified no issues*
- `python manage.py makemigrations --check` → *No changes detected*
- `/index/` e `/cadastro/` respondem com **HTTP 200**

**Autores:**

- Lucas da Fonseca Tavares
- Pedro Guimarães
- Samuel Louven de Senna
