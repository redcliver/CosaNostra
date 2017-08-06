from django.shortcuts import render

# Create your views here.

def venda(request):
    return render(request, 'venda.html', {'title':'Venda'})