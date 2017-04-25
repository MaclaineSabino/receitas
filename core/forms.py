from django import forms
from .models import Receitas

class ReceitaNovaForm(forms.ModelForm):
    class Meta:
        model = Receitas
        fields = ('imagem','nomeprato','ingredientes','modopreparo','qtdpessoas','tempopreparo')
