from django.db import models
from cliente.models import cliente
import datetime
# Create your models here.

class servico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    obs = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

class produto(models.Model):
    TIPOS = (
        ('P', 'Barbearia'),
        ('B', 'Bar'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco_comp = models.DecimalField(max_digits=5, decimal_places=2)
    preco_vend = models.DecimalField(max_digits=5, decimal_places=2)
    qnt = models.IntegerField()
    qnt_minima = models.IntegerField()
    obs = models.CharField(max_length=200, null=True, blank=True)
    tipo = models.CharField(max_length=1, choices=TIPOS)

    def __str__(self):
        return self.nome

class item(models.Model):
    id = models.AutoField(primary_key=True)
    produto1 = models.ForeignKey(produto)
    qnt = models.IntegerField()
    obs = models.CharField(max_length=200, null=True, blank=True)
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.id)

class funcionario(models.Model):
    FUNCAO = (
        ('C', 'Cabelereiro'),
        ('R', 'Recepcionista'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    func = models.CharField(max_length=1, choices=FUNCAO)
    telefone = models.CharField(max_length=15)
    telefone1 = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return self.nome

class servico1(models.Model):
    id = models.AutoField(primary_key=True)
    servico2  = models.ForeignKey(servico)
    funcionario2 = models.ForeignKey(funcionario)

    def __str__(self):
        return self.servico2.nome

class comanda(models.Model):
    STATE = (
        ('O', 'Open'),
        ('C', 'Close'),
    )
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=1, choices=STATE)
    num = models.IntegerField()
    data = models.DateTimeField(default=datetime.datetime.now())
    produtos = models.ManyToManyField(item)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.estado

class comanda_corte(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField(default=datetime.datetime.now())
    servicos = models.ManyToManyField(servico1)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return str(self.id)
