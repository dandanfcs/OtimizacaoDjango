from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    trabalhadores = models.IntegerField()
    fertilizantes = models.IntegerField()
    lucro = models.IntegerField()

