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
    if request.method == 'POST' and request.POST.get('nome') != None:
        nome1 = request.POST.get('nome')
        clientes = cliente.objects.filter(nome__icontains=nome1)
        return render(request, 'editacliente.html', {'title':'Edita cliente', 'clientes':clientes})
    if request.method == 'GET' and request.GET.get('id') != None:
        cliente_id = request.GET.get('id')
        return render(request, 'editacliente1.html', {'title':'Edita cliente','cliente_id':cliente_id})
    return render(request, 'editacliente.html', {'title':'Edita cliente'})

def editacliente1(request):
    cliente_id = request.GET.get('id')
    cliente1 = cliente.objects.filter(id=cliente_id).get()
    if request.method == 'POST':
        cliente_nome = request.POST.get('nome')
        cliente_tel1 = request.POST.get('tel1')
        cliente_tel2 = request.POST.get('tel2')
        cliente1.nome = cliente_nome
        cliente1.telefone1= cliente_tel1
        cliente1.telefone2= cliente_tel2
        cliente1.save()
        msg = "Cliente editado com sucesso!"
        return render(request, 'home/home.html', {'title':'Home','msg':msg})
    return render(request, 'editacliente1.html', {'title':'Edita cliente','cliente1':cliente1})