from django.db import models # type: ignore

class Produto(models.Model):
    nome = models.CharField(max_length=100)  # Nome do produto
    descricao = models.TextField()           # Descrição do produto
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
    validade = models.DateField()            # Data de validade

    def __str__(self):
        return self.nome
