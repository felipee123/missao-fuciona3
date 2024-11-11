from django.db import models # type: ignore

class Produto(models.Model):
    nome = models.CharField(max_length=100)  
    descricao = models.TextField()           
    preco = models.DecimalField(max_digits=10, decimal_places=2)  
    validade = models.DateField()            

    def __str__(self):
        return self.nome
