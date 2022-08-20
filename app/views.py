from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.formProduto import ProdutosForm
from scipy.optimize import linprog
from app.models import Produto
from app.otimizacao import resultado


# Create your views here.
def home(request):
    data = {}
    data['db'] = Produto.objects.all()
    return render(request, 'index.html', data)


def formProduto(request):
    data = {}
    data['form'] = ProdutosForm()
    return render(request, 'formProduto.html', data)


def createProduto(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def otimizacao(request):
    data = {}
    data['obj'] = resultado
    data['produto'] =  Produto.objects.all()
    return render(request, 'otimizacao.html',data)
