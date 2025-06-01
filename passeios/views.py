from django.shortcuts import render, redirect, get_object_or_404
from .models import Passeio
from .forms import PasseioForm
from django.contrib.auth.decorators import login_required
from agendamentos.forms import AgendamentoForm
from agendamentos.models import Agendamento  

@login_required
def agendar_passeio(request, passeio_id):
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

    return render(request, 'passeios/passeio_detalhe.html', {
        'passeio': passeio,
        'form': form
    })

def lista_passeios(request):
    passeios = Passeio.objects.all()
    return render(request, 'passeios/lista.html', {'passeios': passeios})

def criar_passeio(request):
    if request.method == 'POST':
        form = PasseioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_passeios')
    else:
        form = PasseioForm()
    return render(request, 'passeios/form.html', {'form': form})

def editar_passeio(request, pk):
    passeio = get_object_or_404(Passeio, pk=pk)
    if request.method == 'POST':
        form = PasseioForm(request.POST, instance=passeio)
        if form.is_valid():
            form.save()
            return redirect('lista_passeios')
    else:
        form = PasseioForm(instance=passeio)
    return render(request, 'passeios/form.html', {'form': form})

def excluir_passeio(request, pk):
    passeio = get_object_or_404(Passeio, pk=pk)
    if request.method == 'POST':
        passeio.delete()
        return redirect('lista_passeios')
    return render(request, 'passeios/confirmar_exclusao.html', {'passeio': passeio})
