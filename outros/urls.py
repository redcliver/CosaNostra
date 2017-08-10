from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.outros),
    url(r'^addproduto/', views.addproduto),
    url(r'^addservico/', views.addservico),
    url(r'^addservico1/', views.addservico1),
    url(r'^addfuncionario/', views.addfuncionario),
    url(r'^buscacomanda/', views.buscacomanda),
    url(r'^buscacomandacorte/', views.buscacomandacorte),
    ]
