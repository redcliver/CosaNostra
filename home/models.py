from django.db import models
import datetime
# Create your models here.

class servico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.nome

class produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.nome

class item(models.Model):
    id = models.AutoField(primary_key=True)
    produto1 = models.ForeignKey(produto)
    qnt = models.IntegerField()
    obs = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.id

class comanda(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField(default=datetime.datetime.now())
    servicos = models.ManyToManyField(servico)
    produtos = models.ManyToManyField(item)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.id