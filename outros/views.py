from django.shortcuts import render

# Create your views here.

def outros(request):
    return render(request, 'outros.html', {'title':'Outros'})
