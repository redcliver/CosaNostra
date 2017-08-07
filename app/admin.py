from django.contrib import admin
from cliente.models import cliente
from outros.models import produto, comanda, funcionario
from caixa.models import caixa

admin.site.register(cliente)
admin.site.register(produto)
admin.site.register(comanda)
admin.site.register(caixa)
admin.site.register(funcionario)