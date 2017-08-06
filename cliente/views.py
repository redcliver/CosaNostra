from django.shortcuts import render

# Create your views here.

def cliente(request):
    return render(request, 'cliente.html', {'title':'Cliente'})