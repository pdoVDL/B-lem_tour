from django.shortcuts import render, redirect, get_object_or_404
from .models import Agendamento
from .forms import AgendamentoForm
from django.contrib.auth.decorators import login_required
from passeios.models import Passeio
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def cancelar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id, cliente=request.user)

    if request.method == 'POST':
        passeio = agendamento.passeio
        passeio.vagas_disponiveis += agendamento.quantidade_pessoas
        passeio.save()

        agendamento.delete()
        messages.success(request, 'Agendamento cancelado com sucesso.')
        return redirect('meus_agendamentos')

    return render(request, 'agendamentos/confirmar_cancelamento.html', {'agendamento': agendamento})


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

@login_required
def reagendar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id, cliente=request.user)
    passeio = agendamento.passeio
    vagas_atuais = passeio.vagas_disponiveis + agendamento.quantidade_pessoas  # devolve vagas antigas

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            novo_agendamento = form.save(commit=False)

            if novo_agendamento.quantidade_pessoas <= vagas_atuais:
                # Atualiza as vagas corretamente
                passeio.vagas_disponiveis = vagas_atuais - novo_agendamento.quantidade_pessoas
                passeio.save()
                novo_agendamento.save()
                messages.success(request, "Agendamento atualizado com sucesso.")
                return redirect('meus_agendamentos')
            else:
                messages.error(request, f"Não há vagas suficientes. Restam {vagas_atuais}.")
    else:
        form = AgendamentoForm(instance=agendamento)

    return render(request, 'agendamentos/form_reagendar.html', {
        'form': form,
        'agendamento': agendamento
    })
