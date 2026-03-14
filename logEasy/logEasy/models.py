from django.db import models

class Produtos(models.Model):
    nome_produto = models.CharField(max_length=50)
    codigo = models.IntegerField(default=00000)
    quantidade = models.IntegerField(default=00000)

    def __str__(self):
        return self.nome_produto