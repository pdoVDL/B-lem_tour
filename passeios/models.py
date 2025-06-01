from django.db import models

class Passeio(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    local = models.CharField(max_length=100)
    data = models.DateField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.titulo} em {self.local}"