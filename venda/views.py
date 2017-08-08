from django.shortcuts import render
from outros.models import produto, comanda, item
from decimal import *
from caixa.models import caixa


# Create your views here.

def venda(request):
    return render(request, 'venda.html', {'title':'Venda'})

def bar(request):
    return render(request, 'bar.html', {'title':'Bar'})

def produto1(request):
    produtos = produto.objects.all()
    return render(request, 'produto.html', {'title':'Produto', 'produtos':produtos})

def novacomanda(request):
    return render(request, 'novacomanda.html', {'title':'Abrir Comanda'})

def novacomanda1(request):
    comanda1 = request.GET.get('comanda')
    produtos = produto.objects.all()
    if request.method == 'POST':
        comanda2 = request.POST.get('comanda')
        prod = request.POST.get('produto')
        qnt = request.POST.get('qnt')
        prod1 = produto.objects.filter(id=prod).get()
        total1 = prod1.preco*int(qnt)
        criaitem = item(produto1=prod1, qnt=qnt, total=total1)
        criaitem.save()
        teste = item.objects.filter(id=criaitem.id).get()
        criacomanda = comanda(num=comanda2, total=total1, estado='O')
        criacomanda.save()
        criacomanda.produtos.add(teste)
        criacomanda.save()
        msg = "Comanda aberta com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'novacomanda1.html', {'title':'Adicionar Item', 'comanda1':comanda1, 'produtos':produtos})

def additem(request):
    cmd1 = comanda.objects.filter(estado='O')
    return render(request, 'additem.html', {'title':'Adicionar Item', 'cmd1':cmd1})

def additem1(request):
    comanda1 = request.GET.get('comanda')
    cmd1 = comanda.objects.filter(num=comanda1, estado='O').get()
    teste = cmd1.produtos.all()
    produtos = produto.objects.all()
    if request.method == 'POST':
        prod1 = request.POST.get('produto')
        qnt1 = request.POST.get('qnt')
        prod2 = produto.objects.filter(id=prod1).get()
        total1 = prod2.preco*int(qnt1)
        total1 = Decimal(total1)
        teste3 = item(produto1=prod2, qnt=qnt1, total=total1)
        teste3.save()
        cmd1.total = cmd1.total + total1
        teste1 = cmd1.produtos.add(teste3)
        cmd1.save()
        return render(request, 'additem1.html', {'title':'Adicionar Item', 'comanda1':comanda1, 'produtos':produtos, 'teste':teste, 'cmd1':cmd1})
    return render(request, 'additem1.html', {'title':'Adicionar Item', 'comanda1':comanda1, 'produtos':produtos, 'teste':teste, 'cmd1':cmd1})

def fechacomanda(request):
    cmd1 = comanda.objects.filter(estado='O')
    return render(request, 'fechacomanda.html', {'title':'Fechar Comanda', 'cmd1':cmd1})

def fechacomanda1(request):
    comanda1 = request.GET.get('comanda')
    cmd1 = comanda.objects.filter(num=comanda1, estado='O').get()
    teste = cmd1.produtos.all()
    if request.method == 'POST':
        cmd1.estado = 'C'
        cmd1.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+cmd1.total
        desc1 = "Comanda N°: " + str(cmd1.id)
        caixatotal2 = caixa(total=caixatotal1.total, tipo='E', desc=desc1)
        caixatotal2.save()
        msg = "Comanda fechada com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'fechacomanda1.html', {'title':'Conferir Itens', 'comanda1':comanda1, 'teste':teste, 'cmd1':cmd1})