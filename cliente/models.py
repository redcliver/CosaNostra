from django.db import models

# Create your models here.

class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    telefone1 = models.IntegerField()
    telefone2 = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.nome