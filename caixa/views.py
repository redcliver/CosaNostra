from django.shortcuts import render

# Create your views here.

def caixa(request):
    return render(request, 'caixa.html', {'title':'Caixa'})