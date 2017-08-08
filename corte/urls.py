from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.corte1),
    url(r'^imediato/$', views.imediato),
    url(r'^agendado/', views.agendado),
    ]
