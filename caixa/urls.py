from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.caixa1),
    url(r'^extrato/', views.extrato),
    url(r'^retirada/', views.retirada),
    url(r'^fechamento/', views.fechamento),
    ]
