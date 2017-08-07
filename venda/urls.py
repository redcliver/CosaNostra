from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.venda),
    url(r'^bar/$', views.bar),
    url(r'^produto/', views.produto1),
    url(r'^additem/', views.additem),
    url(r'^additem1/', views.additem1),
    url(r'^novacomanda/', views.novacomanda),
    url(r'^novacomanda1/', views.novacomanda1),
    url(r'^fechacomanda/', views.fechacomanda),
    url(r'^fechacomanda1/', views.fechacomanda1),
    ]
