from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtos
from .forms import ProdutosForm

def recebimento(request):
    form = ProdutosForm()
    return render(request, 'recebimento.html')
    

def editar_produto(request, pk):
    #busca item pelo ID
    item = get_object_or_404(Produtos, pk=pk)
    if request.method == 'POST':
        form = ProdutosForm(request.POST, instance=item)
        if form.is_valid():
            form.save() #executa o comando UPDATE no sql
            return redirect('listar_produto')
    else:
        #No get, op instance=item pré preenche os dados do banco
        form = ProdutosForm(instance=item)
    return render(request, 'editar.html', {'form':form})





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