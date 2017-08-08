from django.db import models
import datetime

# Create your models here.

class caixa(models.Model):
    TIPO = (
        ('E', 'Entrada'),
        ('S', 'Saida'),
    )
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=1, choices=TIPO)
    data = models.DateTimeField(default=datetime.datetime.now())
    desc = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.id)
