# This Python file uses the following encoding: utf-8
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2c5c0fdc608863fa415c4b50c76304f53e54bb5a
# ANOTAÇÃO PARA USAR CARACTERES ESPECIAIS AQUI. (MESMO PARA ANOTAÇÕES.)

from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q #Queries complexas
from pessoas.models import Pessoa

<<<<<<< HEAD
=======
=======
"""
@israel.frp
https://www.facebook.com/israel.frp
"""

from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from pessoas.models import Pessoa


>>>>>>> ed271e821956b564a159ec5d478d3e7c31ad071e
>>>>>>> 2c5c0fdc608863fa415c4b50c76304f53e54bb5a
def index(request):
    return render(request, 'index.html')

def pessoaListar(request):
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2c5c0fdc608863fa415c4b50c76304f53e54bb5a
    pessoas = Pessoa.objects.all()[0:10]

    return render(request, 'pessoas/listaPessoas.html', {'pessoas': pessoas})


<<<<<<< HEAD
=======
=======
    pessoas = Pessoa.objects.all().order_by('nome')[0:10]
    return render(request, 'pessoas/listaPessoas.html', {'pessoas': pessoas})

>>>>>>> ed271e821956b564a159ec5d478d3e7c31ad071e
>>>>>>> 2c5c0fdc608863fa415c4b50c76304f53e54bb5a
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

def pessoaPesquisar(request):
    if request.method == 'POST':
        textoBusca = request.POST.get('textoBusca', 'TUDO').upper()

        try:
            if textoBusca == 'TUDO':
                pessoas = Pessoa.objects.all()
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2c5c0fdc608863fa415c4b50c76304f53e54bb5a
            else: 
                pessoas = Pessoa.objects.filter(
                    (Q(nome__contains=textoBusca) |  
                    Q(email__contains=textoBusca) | 
                    Q(telefone__contains=textoBusca) | 
                    Q(logradouro__contains=textoBusca))).order_by('-nome')  #BUSCA POR NOME OU EMAIL OU TELEFONE OU LOGRADOURO... E É ORDENADO POR NOME.
<<<<<<< HEAD
=======
=======
            else:
                pessoas = Pessoa.objects.filter(
                    (Q(nome__contains=textoBusca) |
                    Q(email__contains=textoBusca) |
                    Q(telefone__contains=textoBusca) |
                    Q(logradouro__contains=textoBusca))).order_by('nome') #BUSCA POR NOME OU EMAIL OU TELEFONE OU LOGRADOURO... E É ORDENADO POR NOME.
>>>>>>> ed271e821956b564a159ec5d478d3e7c31ad071e
>>>>>>> 2c5c0fdc608863fa415c4b50c76304f53e54bb5a
        except:
            pessoas = []

        return render(request, 'pessoas/listaPessoas.html', {'pessoas': pessoas, 'textoBusca': textoBusca})

def pessoaEditar(request, pk=0):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except:
        return HttpResponseRedirect('/pessoas/')

    return render(request, 'pessoas/formPessoas.html', {'pessoa': pessoa})

def pessoaExcluir(request, pk=0):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
        pessoa.delete()
        return HttpResponseRedirect('/pessoas/')
    except:
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2c5c0fdc608863fa415c4b50c76304f53e54bb5a
        return HttpResponseRedirect('/pessoas/')




    




<<<<<<< HEAD
=======
=======
        return HttpResponseRedirect('/pessoas/')
>>>>>>> ed271e821956b564a159ec5d478d3e7c31ad071e
>>>>>>> 2c5c0fdc608863fa415c4b50c76304f53e54bb5a
