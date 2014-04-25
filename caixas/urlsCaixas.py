<<<<<<< HEAD
=======
<<<<<<< HEAD
from django.conf.urls import patterns, include, url

urlpatterns = patterns('caixas.views',
    url(r'^adicionar/$', 'contaAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'contaEditar'),
    url(r'^salvar/$', 'contaSalvar'),
    url(r'^pesquisar/$', 'contaPesquisar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'contaExcluir'),
    url(r'^$', 'contaListar'),
=======
>>>>>>> 2c5c0fdc608863fa415c4b50c76304f53e54bb5a
from django.conf.urls import patterns, include, url

urlpatterns = patterns('caixas.views',
    url(r'^adicionar/$', 'contaAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'contaEditar'),
    url(r'^salvar/$', 'contaSalvar'),
    url(r'^pesquisar/$', 'contaPesquisar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'contaExcluir'),
    url(r'^$', 'contaListar'),
<<<<<<< HEAD
=======
>>>>>>> ed271e821956b564a159ec5d478d3e7c31ad071e
>>>>>>> 2c5c0fdc608863fa415c4b50c76304f53e54bb5a
)