from django.db import models
from django.contrib.auth.models import User

class Passeio(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    local = models.CharField(max_length=100)
    data = models.DateField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    vagas_disponiveis = models.PositiveIntegerField(default=10) 

    def __str__(self):
        return f"{self.titulo} em {self.local}"
    
class Avaliacao(models.Model):
    passeio = models.ForeignKey(Passeio, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comentario = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.nota}⭐ para {self.passeio.titulo}"