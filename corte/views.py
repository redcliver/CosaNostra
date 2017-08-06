from django.shortcuts import render

# Create your views here.

def corte(request):
    return render(request, 'corte.html', {'title':'Corte'})