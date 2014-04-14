# This Python file uses the following encoding: utf-8
"""
@israel.frp
https://www.facebook.com/israel.frp
"""

from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from pessoas.models import Pessoa


def index(request):
    return render(request, 'index.html')

def pessoaListar(request):
    pessoas = Pessoa.objects.all()[0:10]
    return render(request, 'pessoas/listaPessoas.html', {'pessoas': pessoas})

def pessoaAdicionar(request):
    return render(request, 'pessoas/formPessoas.html')

def pessoaSalvar(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '0')

        try:
            pessoa = Pessoa.objects.get(pk=codigo)
        except:
            pessoa = Pessoa()

        pessoa.nome = request.POST.get('nome', '').upper()
        pessoa.email = request.POST.get('email', '').upper()
        pessoa.telefone = request.POST.get('telefone', '(00) 0-0000-0000').upper()
        pessoa.logradouro = request.POST.get('logradouro', '').upper()

        pessoa.save()
        return HttpResponseRedirect('/pessoas/')