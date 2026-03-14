from django.shortcuts import render, redirect
from .forms import ProdutosForm

def recebimento(request):
    form = ProdutosForm()
    return render(request, 'recebimento.html')

def index(request):
    return render(request, "index.html")

def produtos_view(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recebimento')
    
    else:
        form = ProdutosForm()
    
    return render(request, 'recebimento.html', {'form': form})