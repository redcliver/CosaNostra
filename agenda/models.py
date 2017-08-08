from django.db import models
import datetime
from cliente.models import cliente
from outros.models import funcionario, servico
# Create your models here.

class agenda (models.Model):
    CONF = (
        ('S', 'Sim'),
        ('N', 'Nao'),
    )
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField()
    cliente1 = models.ForeignKey(cliente)
    func1 = models.ForeignKey(funcionario)
    servico1 = models.ForeignKey(servico)
    confirmado = models.CharField(max_length=1, choices=CONF)

    def __str__(self):
        return str(self.id)