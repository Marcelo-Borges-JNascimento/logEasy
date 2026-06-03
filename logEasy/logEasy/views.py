from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtos
from .forms import ProdutosForm
from django.contrib import messages
from .models import Produtos, HistoricoExpedicao

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

def expedicao(request):
    return render(request, 'expedicao.html')

def listar_P2(request):
    produtos = Produtos.objects.all()
    return render(request, 'expedicao.html', {'produtos': produtos})

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Produtos

def processar_saida_estoque(request, produto_id):
    if request.method == 'POST':
        # 1. Busca o produto clicado no banco de dados
        produto = get_object_or_404(Produtos, id=produto_id)
        
        # 2. Pega a quantidade que o usuário digitou no input 'qnt_saida'
        quantidade_saida_str = request.POST.get('qnt_saida')
        
        # Validação simples para garantir que veio um número
        if not quantidade_saida_str:
            messages.error(request, "Por favor, digite uma quantidade.")
            return redirect('listar_P2') # Substitua pelo nome da sua URL de expedição
            
        quantidade_saida = int(quantidade_saida_str)

        # 3. Regra de negócio: impede tirar mais do que tem no estoque
        if quantidade_saida > produto.quantidade:
            messages.error(request, f"Erro: Estoque insuficiente de {produto.nome_produto}!")
            return redirect('listar_P2')
        
        # Registrar o log na tabela HistoricoExpedicao
        HistoricoExpedicao.objects.create(
            produto_nome=produto.nome_produto,
            codigo_produto=produto.codigo,
            departamento_nome=produto.departamento.nome if produto.departamento else "Sem Departamento",
            quantidade_retirada=quantidade_saida
        )

        # 4. Faz a subtração
        nova_quantidade = produto.quantidade - quantidade_saida
        
        # 5. Verifica se o produto zerou ou se apenas diminuiu
        if nova_quantidade <= 0:
            produto.delete() # Se zerou, remove a linha do banco de dados
            messages.success(request, f"{produto.nome_produto} foi totalmente expedido e removido do estoque.")
        else:
            produto.quantidade = nova_quantidade
            produto.save() # Salva a nova quantidade diminuída no MySQL
            messages.success(request, f"Saída de {quantidade_saida} unidades de {produto.nome_produto} realizada.")
            
    return redirect('listar_P2') # Recarrega a página atualizada
