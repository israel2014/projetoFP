from django.shortcuts import render
from pessoas.models import Pessoa


def index(request):
    return render(request, 'index.html')

def pessoaListar(request):
    pessoas = Pessoa.objects.all()[0:10]
    return render(request, 'pessoas/listaPessoas.html', {'pessoas': pessoas})