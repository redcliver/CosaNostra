from django.shortcuts import render
from agenda.models import agenda
import datetime
from outros.models import comanda_corte, servico1
from caixa.models import caixa
# Create your views here.

def agenda1(request):
    hoje = datetime.date.today()
    agendas = agenda.objects.filter(data__icontains=hoje, confirmado='N')
    
    if request.method == 'POST':
        hoje = request.POST.get('data')
        agendas = agenda.objects.filter(data__icontains=hoje, confirmado='N')
        return render(request, 'agenda.html', {'title':'Agenda', 'agendas':agendas, 'hoje':hoje})
    return render(request, 'agenda.html', {'title':'Agenda', 'agendas':agendas, 'hoje':hoje})

def confirmacao(request):
    num = request.POST.get('confirmacao')
    cli = agenda.objects.filter(id=num).get()
    cli.confirmado = 'S'
    cli.save()
    serv1 = cli.servico1
    func1 = cli.func1
    serv2 = servico1(servico2=serv1, funcionario2=func1)
    serv2.save()
    total1 = cli.servico1.preco
    comanda1 = comanda_corte(total=total1)
    comanda1.save()
    comanda1.servicos.add(serv2)
    comanda1.save()
    caixatotal1 = caixa.objects.latest('id')
    caixatotal1.total = caixatotal1.total+comanda1.total
    desc1 = "Comanda_corte N°: " + str(comanda1.id)
    caixatotal2 = caixa(total=caixatotal1.total, tipo='E', desc=desc1)
    caixatotal2.save()
    msg = "Cliente confirmado com sucesso"
    return render(request, 'home/home.html', {'title':'Home', 'msg':msg})