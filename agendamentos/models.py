from django.db import models
from django.contrib.auth.models import User
from passeios.models import Passeio

class Agendamento(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    passeio = models.ForeignKey(Passeio, on_delete=models.CASCADE)
    data_agendada = models.DateField()
    quantidade_pessoas = models.PositiveIntegerField()
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cliente.username} - {self.passeio.titulo} em {self.data_agendada}"
