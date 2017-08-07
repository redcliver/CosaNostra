from django.shortcuts import render
import datetime
from cliente.models import cliente
from outros.models import funcionario

# Create your views here.

def corte(request):
    return render(request, 'corte.html', {'title':'Corte'})

def imediato(request):
    clientes = cliente.objects.all()
    funcionarios = funcionario.objects.all().filter(func='C')
    if request.method == 'POST':
        cliente1 = request.POST.get('cliente')
        func1 =request.POST.get('funcionario')
        serv1 =request.POST.get('corte')
        cliente2 = cliente.objects.filter(id=cliente1).get()
        func2 = funcionario.objects.filter(id=func1).get()
         
    return render(request, 'imediato.html', {'title':'Corte', 'clientes':clientes, 'funcionarios':funcionarios})

def agendado(request):
    hoje = datetime.datetime.now()
    return render(request, 'agendado.html', {'title':'Corte', 'hoje':hoje})