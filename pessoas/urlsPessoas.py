<<<<<<< HEAD
=======
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
>>>>>>> 2c5c0fdc608863fa415c4b50c76304f53e54bb5a
from django.conf.urls import patterns, include, url

urlpatterns = patterns('pessoas.views',
    url(r'^adicionar/$', 'pessoaAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'pessoaEditar'),
    url(r'^salvar/$', 'pessoaSalvar'),
    url(r'^pesquisar/$', 'pessoaPesquisar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'pessoaExcluir'),
    url(r'^$', 'pessoaListar'),
<<<<<<< HEAD
=======
>>>>>>> ed271e821956b564a159ec5d478d3e7c31ad071e
>>>>>>> 2c5c0fdc608863fa415c4b50c76304f53e54bb5a
)