from django.shortcuts import render
from cliente.models import cliente

# Create your views here.

def cliente1(request):
    return render(request, 'cliente.html', {'title':'Cliente'})

def addcliente(request):
    if request.method == 'POST':
        nome1 = request.POST.get('nome')
        tel2 = request.POST.get('tel1')
        tel3 = request.POST.get('tel2')
        cliente1 = cliente(nome=nome1, telefone1=tel2, telefone2=tel3)
        cliente1.save()
        msg = "Cliente registrado com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'addcliente.html', {'title':'Adiciona cliente'})



def buscacliente(request):
    if request.method == 'POST':
        nome1 = request.POST.get('nome')
        clientes = cliente.objects.filter(nome__icontains=nome1)
        return render(request, 'buscacliente.html', {'title':'Buscar cliente', 'clientes':clientes})
    return render(request, 'buscacliente.html', {'title':'Buscar cliente'})

def editacliente(request):
    return render(request, 'editacliente.html', {'title':'Edita cliente'})