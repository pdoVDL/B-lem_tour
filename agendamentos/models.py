from django.db import models
from django.contrib.auth.models import User
from django.apps import apps


class Agendamento(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    passeio = models.ForeignKey('passeios.Passeio', on_delete=models.CASCADE)  # ✅ referência por string
    data_agendada = models.DateField()
    quantidade_pessoas = models.PositiveIntegerField()
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cliente.username} - {self.passeio.titulo} em {self.data_agendada}"

