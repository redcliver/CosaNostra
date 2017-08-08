from django.shortcuts import render
from .models import caixa
import datetime
# Create your views here.

def caixa1(request):
    total = caixa.objects.latest('id')
    return render(request, 'caixa.html', {'title':'Caixa', 'total':total})

def extrato(request):
    hoje = datetime.date.today()
    caixas = caixa.objects.filter(data__contains=hoje)
    return render(request, 'extrato.html', {'title':'Extrato', 'caixas':caixas})