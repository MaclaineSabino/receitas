from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from .models import Receitas
from .forms import ReceitaNovaForm

def inicio(request):

    receitas = Receitas.objects.all()

    return render(request,'core/inicio.html',{'receitas':receitas})

def receitadetalhe(request,pk):

    receit = get_object_or_404(Receitas,pk=pk)

    return render(request,'core/receitadetalhe.html',{'receit':receit})

def edicoes(request):
    receitas = Receitas.objects.all()

    return render(request,'core/editar.html',{'receitas':receitas})

def excluir(request):
    receitas = Receitas.objects.all()

    return render(request,'core/excluir.html',{'receitas':receitas})

def listar(request):
    valor = request.POST.get('campo_busca')
    receitas = Receitas.objects.filter(Q(nomeprato__contains=valor) | Q(tempopreparo__contains=valor)).distinct()
    return render(request,'core/listar.html',{'receitas':receitas})

def receita_nova(request):
    if request.method=="POST":
        form = ReceitaNovaForm(request.POST)
        if form.is_valid():
            postagem = form.save()
            return redirect('receitadet', pk=postagem.pk)

    else:
        form = ReceitaNovaForm()
    return render(request, 'core/novarec.html',{'form':form})

def receita_edit(request,pk):
    recei = get_object_or_404(Receitas,pk=pk)
    if request.method=="POST":
        form = ReceitaNovaForm(request.POST,instance=recei)
        if form.is_valid():
            postagem = form.save()
            return redirect('receitadet', pk=postagem.pk)
    else:
        form = ReceitaNovaForm(instance=recei)

    return render(request, 'core/novarec.html',{'form':form}) # o mesmo formulário de inserir receitas foi usado
#para edição

def receita_excluir(request,pk):
    Receitas.objects.filter(pk=pk).delete()
    return redirect('excluir') #ao excluir a página é redirecionada para a mesma página de exclusões


# Create your views here.
