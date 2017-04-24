from django.db import models

class Receitas(models.Model):
    imagem = models.CharField(max_length=200, default='null.jpg')
    nomeprato = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modopreparo = models.TextField()
    qtdpessoas = models.IntegerField()
    tempopreparo = models.IntegerField()

    def __str__(self):

        return self.nomeprato


# Create your models here.
