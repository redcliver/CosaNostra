from django.shortcuts import render
from .models import produto, servico, funcionario, comanda, comanda_corte, item

# Create your views here.

def outros(request):
    return render(request, 'outros.html', {'title':'Outros'})

def addproduto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        tipo = request.POST.get('tipo')
        obs = request.POST.get('obs')
        produto1 = produto(nome=nome, preco=preco, tipo=tipo, obs=obs)
        produto1.save()
        msg = "Produto cadastrado com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'addproduto.html', {'title':'Adicionar Produto'})


def addservico(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        obs = request.POST.get('obs')
        servico1 = servico(nome=nome, preco=preco, obs=obs)
        servico1.save()
        msg = "Servico cadastrado com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'addservico.html', {'title':'Adicionar Servico'})

def addfuncionario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        func = request.POST.get('func')
        tel1 = request.POST.get('tel1')
        tel2 = request.POST.get('tel2')
        func1 = funcionario(nome=nome, func=func, telefone=tel1, telefone1=tel2)
        func1.save()
        msg = "Funcionario Registrado com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'addfuncionario.html', {'title':'Adicionar Funcionario'})

def buscacomanda(request):
    if request.method == 'POST':
        comanda1 = request.POST.get('comanda')
        comanda1 = int(comanda1)
        cmd1 = comanda.objects.filter(id=comanda1).get()
        teste = cmd1.produtos.all()
        return render(request, 'buscacomanda.html', {'title':'Buscar comanda', 'cmd1':cmd1, 'teste':teste})
    if request.method == 'GET' and request.GET.get('item') != None:
        item1 = request.GET.get('item')
        comanda1 = request.GET.get('comanda')
        cmd2 = comanda.objects.filter(id=comanda1).get()
        item2 = item.objects.filter(id=item1).get()
        cmd2.total = cmd2.total-item2.produto1.preco
        cmd2.save()
        item2.delete()
        msg = "Item deletado com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'buscacomanda.html', {'title':'Buscar comanda bar'})

def buscacomandacorte(request):
    if request.method == 'POST':
        comanda1 = request.POST.get('comanda')
        comanda1 = int(comanda1)
        cmd1 = comanda_corte.objects.filter(id=comanda1).get()
        teste = cmd1.servicos.all()
        return render(request, 'buscacomandacorte.html', {'title':'Buscar comanda corte', 'cmd1':cmd1, 'teste':teste})
    return render(request, 'buscacomandacorte.html', {'title':'Buscar comanda corte'})