from django.conf.urls import include, url
from .import views


urlpatterns = [

    url(r'^$', views.inicio, name='home'),
    url(r'^receitas/(?P<pk>[0-9]+)/$', views.receitadetalhe, name='receitadet'),
    url(r'^receita/nova/$',views.receita_nova, name='receita_nova'),
    url(r'^receitas/(?P<pk>[0-9]+)/editar/$', views.receita_edit, name='receita_editar'),
    url(r'^receita/editar/$', views.edicoes, name='editar'),
    url(r'^receita/excluir/$', views.excluir, name='excluir'),
    url(r'^receita/listar/$', views.listar, name='listar'),
    url(r'^receita/exclusoes/(?P<pk>[0-9]+)/$', views.receita_excluir, name='receita_excluir'),

]
