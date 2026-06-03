# from django.db import models

# class Produtos(models.Model):
#     nome_produto = models.CharField(max_length=50)
#     codigo = models.IntegerField(default=00000)
#     quantidade = models.IntegerField(default=00000)
#     # Criar o campo "departamento" para que seja possível criar novas tabelas que se relacionem com ele;
#     def __str__(self):
#         return self.nome_produto
    
#     # tabela departamentos - Onde irá constar a lista de departamentos que irão 

#     # Classe Perfumaria
#         # logica - Se o produto tiver o departamento correspondente, a classe atual deve buscar o produto dentro da classe produtos
#     # Classe Higiene

from django.db import models

# Tabela Departamento
class Departamento(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

#Tabela de produtos (que puxa a FK de Departamento)
class Produtos(models.Model):
    nome_produto = models.CharField(max_length=50)
    codigo = models.IntegerField(default=0)
    quantidade = models.IntegerField(default=0)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='produtos', null=True, blank=True)

    def __str__(self):
        return self.nome_produto

# Tabela de Logs
class HistoricoExpedicao(models.Model):
    produto_nome = models.CharField(max_length=100)
    codigo_produto = models.IntegerField()
    departamento_nome = models.CharField(max_length=50)
    quantidade_retirada = models.IntegerField()
    data_saida = models.DateTimeField(auto_now_add=True)