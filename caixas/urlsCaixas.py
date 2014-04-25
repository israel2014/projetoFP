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
from django.conf.urls import patterns, include, url

urlpatterns = patterns('caixas.views',
    url(r'^adicionar/$', 'contaAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'contaEditar'),
    url(r'^salvar/$', 'contaSalvar'),
    url(r'^pesquisar/$', 'contaPesquisar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'contaExcluir'),
    url(r'^$', 'contaListar'),
>>>>>>> ed271e821956b564a159ec5d478d3e7c31ad071e
)