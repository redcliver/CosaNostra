from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.outros),
    url(r'^addproduto/', views.addproduto),
    url(r'^addproduto1/', views.addproduto1),
    url(r'^addservico/', views.addservico),
    url(r'^addservico1/', views.addservico1),
    url(r'^addfuncionario/', views.addfuncionario),
    url(r'^addfuncionario1/', views.addfuncionario1),
    url(r'^buscacomanda/', views.buscacomanda),
    url(r'^buscacomandacorte/', views.buscacomandacorte),
    ]
