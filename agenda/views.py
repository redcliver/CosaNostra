from django.shortcuts import render

# Create your views here.

def agenda(request):
    return render(request, 'agenda.html', {'title':'Agenda'})