from django.shortcuts import render
import datetime
from caixa.models import caixa
from cliente.models import cliente
from outros.models import funcionario, servico1, servico, comanda_corte
from agenda.models import agenda

# Create your views here.

def corte1(request):
    return render(request, 'corte1.html', {'title':'Corte'} )

def imediato(request):
    clientes = cliente.objects.all()
    funcionarios = funcionario.objects.all().filter(func='C')
    if request.method == 'POST':
        cliente1 = request.POST.get('cliente')
        func1 =request.POST.get('funcionario')
        serv1 =request.POST.get('corte')
        cliente2 = cliente.objects.filter(id=cliente1).get()
        func2 = funcionario.objects.filter(id=func1).get()
        serv2 = servico.objects.filter(obs=serv1).get()
        serv = servico1(servico2=serv2, funcionario2=func2)
        serv.save()
        total1 = serv2.preco
        comanda1 = comanda_corte(total=total1)
        comanda1.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+comanda1.total
        desc1 = "Comanda_Corte N°: " + str(comanda1.id)
        caixatotal2 = caixa(total=caixatotal1.total, tipo='E', desc=desc1)
        caixatotal2.save()
        comanda1.servicos.add(serv)
        comanda1.save()
        msg = "Corte registrado com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg} )
    return render(request, 'imediato.html', {'title':'Corte', 'clientes':clientes, 'funcionarios':funcionarios})

def imediato1(request):
    cliente1 = request.GET.get('cliente')
    func1 =request.GET.get('funcionario')
    serv1 =request.GET.get('corte')

    return render(request, 'imediato1.html', {'title':'Corte'})

def agendado(request):
    hoje = datetime.datetime.now()
    clientes = cliente.objects.all()
    funcionarios = funcionario.objects.all().filter(func='C')
    if request.method == 'POST':
        cliente1 = request.POST.get('cliente')
        func1 =request.POST.get('funcionario')
        serv1 =request.POST.get('corte')
        data1 =request.POST.get('data')
        cliente2 = cliente.objects.filter(id=cliente1).get()
        func2 = funcionario.objects.filter(id=func1).get()
        serv2 = servico.objects.filter(obs=serv1).get()
        agenda1 = agenda(cliente1=cliente2, func1=func2, servico1=serv2, data=data1, confirmado='N')
        agenda1.save()
        msg = "Corte agendado com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg} )
    return render(request, 'agendado.html', {'title':'Corte', 'hoje':hoje, 'clientes':clientes, 'funcionarios':funcionarios})