from django.shortcuts import render
from .models import produto, servico, funcionario, comanda, comanda_corte

# Create your views here.

def outros(request):
    return render(request, 'outros.html', {'title':'Outros'})

def addproduto(request):
    return render(request, 'addproduto.html', {'title':'Adicionar Produto'})

def addproduto1(request):
    nome = request.GET.get('nome')
    preco = request.GET.get('preco')
    tipo = request.GET.get('tipo')
    obs = request.GET.get('obs')
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        tipo = request.POST.get('tipo')
        obs = request.POST.get('obs')
        produto1 = produto(nome=nome, preco=preco, tipo=tipo, obs=obs)
        produto1.save()
        msg = "Produto cadastrado com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'addproduto1.html', {'title':'Adicionar Produto', 'nome':nome, 'preco':preco, 'tipo':tipo, 'obs':obs})

def addservico(request):
    return render(request, 'addservico.html', {'title':'Adicionar Servico'})

def addservico1(request):
    nome = request.GET.get('nome')
    preco = request.GET.get('preco')
    obs = request.GET.get('obs')
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        obs = request.POST.get('obs')
        servico1 = servico(nome=nome, preco=preco, obs=obs)
        servico1.save()
        msg = "Servico cadastrado com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'addservico1.html', {'title':'Confirmar Servico', 'nome':nome, 'preco':preco, 'obs':obs})

def addfuncionario(request):
    return render(request, 'addfuncionario.html', {'title':'Adicionar Funcionario'})

def addfuncionario1(request):
    nome = request.GET.get('nome')
    func = request.GET.get('func')
    tel1 = request.GET.get('tel1')
    tel2 = request.GET.get('tel2')
    if request.method == 'POST':
        nome = request.POST.get('nome')
        func = request.POST.get('func')
        tel1 = request.POST.get('tel1')
        tel2 = request.POST.get('tel2')
        func1 = funcionario(nome=nome, func=func, telefone=tel1, telefone1=tel2)
        func1.save()
        msg = "Funcionario Registrado com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'addfuncionario1.html', {'title':'Confirma Funcionario', 'nome':nome, 'func':func, 'tel1':tel1, 'tel2':tel2})

def buscacomanda(request):
    if request.method == 'POST':
        comanda1 = request.POST.get('comanda')
        comanda1 = int(comanda1)
        cmd1 = comanda.objects.filter(id=comanda1).get()
        teste = cmd1.produtos.all()
        return render(request, 'buscacomanda.html', {'title':'Buscar comanda', 'cmd1':cmd1, 'teste':teste})
    return render(request, 'buscacomanda.html', {'title':'Buscar comanda bar'})

def buscacomandacorte(request):
    if request.method == 'POST':
        comanda1 = request.POST.get('comanda')
        comanda1 = int(comanda1)
        cmd1 = comanda_corte.objects.filter(id=comanda1).get()
        teste = cmd1.servicos.all()
        return render(request, 'buscacomandacorte.html', {'title':'Buscar comanda corte', 'cmd1':cmd1, 'teste':teste})
    return render(request, 'buscacomandacorte.html', {'title':'Buscar comanda corte'})