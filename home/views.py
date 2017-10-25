from django.shortcuts import render
from twilio.rest import Client
# Create your views here.

def home(request):
    # Your Account SID from twilio.com/console
    account_sid = "AC3074d1e8f313b884f1be5b4b8f47d6c2"
    # Your Auth Token from twilio.com/console
    auth_token  = "3f8d71550aa6731e856291f76da6e030"

    client = Client(account_sid, auth_token)
    msg1 = "Este e um teste de msg"
    message = client.messages.create(to="+5567991865754", from_="(559) 869-4092",body=msg1)
    msg = "Mensagem enviada com sucesso!"
    return render(request, 'home/home.html', {'title':'Home', 'msg':msg})

