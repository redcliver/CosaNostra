from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.agenda1),
    url(r'^confirmacao$', views.confirmacao),
    ]
