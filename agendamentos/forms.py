from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['passeio', 'data_agendada', 'quantidade_pessoas']
        widgets = {
            'data_agendada': forms.DateInput(attrs={'type': 'date'}),
        }
