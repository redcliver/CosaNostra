from django.shortcuts import render
from .models import caixa
from outros.models import comanda_corte, funcionario, servico1
import datetime
from decimal import *
# Create your views here.

def caixa1(request):
    total = caixa.objects.latest('id')
    return render(request, 'caixa.html', {'title':'Caixa', 'total':total})

def extrato(request):
    hoje = datetime.date.today()
    caixas = caixa.objects.filter(data__contains=hoje)
    return render(request, 'extrato.html', {'title':'Extrato', 'caixas':caixas})

def retirada(request):
    total = caixa.objects.latest('id')
    if request.method == 'POST':
        valor = request.POST.get('valor')
        motivo = request.POST.get('obs')
        total1 = total.total
        total2 = total1 - Decimal(valor)
        retirada1 = caixa(total=total2, desc=motivo, tipo='S')
        retirada1.save()
        msg = "Retirada efetuada com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'retirada.html', {'title':'Retirada', 'total':total})

def fechamento(request):
    total = caixa.objects.latest('id')
    if request.method == 'POST':
        valor = request.POST.get('valor')
        motivo = "Fechamento"
        total1 = total.total
        total2 = total1 - Decimal(valor)
        retirada1 = caixa(total=total2, desc=motivo, tipo='S')
        retirada1.save()
        msg = "Caixa fechado com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'fechamento.html', {'title':'Fechamento', 'total':total})

def extratodetalhado(request):
    hoje = datetime.date.today()
    jeff = funcionario.objects.filter(nome__icontains="jef").get()
    rubens = funcionario.objects.filter(nome__icontains="rub").get()
    cmd_jefferson = servico1.objects.all().filter(funcionario2__nome=jeff, comanda_corte__data__icontains=hoje)
    cmd_rubens = servico1.objects.all().filter(funcionario2__nome=rubens, comanda_corte__data__icontains=hoje)
    return render(request, 'extratodetalhado.html', {'title':'Extrato detalhado', 'cmd_jefferson':cmd_jefferson, 'cmd_rubens':cmd_rubens})