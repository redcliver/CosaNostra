from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.cliente1),
    url(r'^addcliente/', views.addcliente),
    url(r'^addcliente1/', views.addcliente1),
    url(r'^buscacliente/', views.buscacliente),
    ]
