from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    discricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)
    

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

class Usuarios(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    metas = models.TextField(null=True,blank=True)
    salario = models.IntegerField(null=False)

