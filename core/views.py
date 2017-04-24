from django.shortcuts import render
from .models import Receitas

def inicio(request):

    receitas = Receitas.objects.all()
    return render(request,'core/inicio.html',{'receitas':receitas})
# Create your views here.
