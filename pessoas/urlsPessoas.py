<<<<<<< HEAD
from django.conf.urls import patterns, include, url

urlpatterns = patterns('pessoas.views',
    url(r'^adicionar/$', 'pessoaAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'pessoaEditar'),
    url(r'^salvar/$', 'pessoaSalvar'),
    url(r'^pesquisar/$', 'pessoaPesquisar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'pessoaExcluir'),
    url(r'^$', 'pessoaListar'),
=======
from django.conf.urls import patterns, include, url

urlpatterns = patterns('pessoas.views',
    url(r'^adicionar/$', 'pessoaAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'pessoaEditar'),
    url(r'^salvar/$', 'pessoaSalvar'),
    url(r'^pesquisar/$', 'pessoaPesquisar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'pessoaExcluir'),
    url(r'^$', 'pessoaListar'),
>>>>>>> ed271e821956b564a159ec5d478d3e7c31ad071e
)