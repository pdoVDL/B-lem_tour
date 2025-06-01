from django import forms
from .models import Passeio

class PasseioForm(forms.ModelForm):
    class Meta:
        model = Passeio
        fields = ['titulo', 'descricao','local', 'data', 'preco']