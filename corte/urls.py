from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.corte),
    url(r'^imediato/', views.imediato),
    ##url(r'^imediato1/', views.imediato1),
    url(r'^agendado/', views.agendado),
    ]
