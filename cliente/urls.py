from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.cliente1),
    url(r'^addcliente/', views.addcliente),
    url(r'^buscacliente/', views.buscacliente),
    url(r'^editacliente/', views.editacliente),
    ]
