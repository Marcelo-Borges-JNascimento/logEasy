from django.shortcuts import render, redirect
from .models import Produtos
from .forms import ProdutosForm

def recebimento(request):
    form = ProdutosForm()
    return render(request, 'recebimento.html')

def index(request):
    return render(request, "index.html")

def estoque(request):
    return render(request, "estoque.html")

def listar_produto(request):
    #busca todos os produtos da tabela:
    produtos = Produtos.objects.all()
    return render(request, 'estoque.html', {'produtos': produtos})

def produtos_view(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recebimento')
    
    else:
        form = ProdutosForm()
    
    return render(request, 'recebimento.html', {'form': form})