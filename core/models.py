from django.db import models

class Receitas(models.Model):
    nomeprato = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modopreparo = models.TextField()
    qtdpessoas = models.IntegerField()
    tempopreparo = models.TimeField()

    def __str__(self):

        return self.nomeprato


# Create your models here.
