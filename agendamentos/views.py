from django.shortcuts import render, redirect, get_object_or_404
from .models import Agendamento
from .forms import AgendamentoForm
from django.contrib.auth.decorators import login_required
from passeios.models import Passeio

def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamentos/lista.html', {'agendamentos': agendamentos})


@login_required
def criar_agendamento_com_passeio(request, passeio_id):
    passeio = get_object_or_404(Passeio, id=passeio_id)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.cliente = request.user
            agendamento.passeio = passeio
            agendamento.save()
            return redirect('meus_agendamentos')
    else:
        form = AgendamentoForm()

    return render(request, 'agendamentos/form.html', {
        'form': form,
        'passeio': passeio
    })

@login_required
def meus_agendamentos(request):
    agendamentos = Agendamento.objects.filter(cliente=request.user)
    return render(request, 'agendamentos/meus.html', {'agendamentos': agendamentos})


def editar_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'agendamentos/form.html', {'form': form})

def excluir_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('lista_agendamentos')
    return render(request, 'agendamentos/confirmar_exclusao.html', {'agendamento': agendamento})
