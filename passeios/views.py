from django.shortcuts import render, redirect, get_object_or_404
from .models import Passeio
from .forms import PasseioForm
from passeios.forms import AvaliacaoForm  
from django.contrib.auth.decorators import login_required
from agendamentos.forms import AgendamentoForm
from agendamentos.models import Agendamento  
from django.contrib import messages
from .models import Passeio, Avaliacao

def detalhe_passeio(request, passeio_id):
    passeio = get_object_or_404(Passeio, id=passeio_id)

    agendamento_form = AgendamentoForm()
    avaliacao_form = AvaliacaoForm()

    # Agendamento
    if request.method == 'POST' and 'agendar' in request.POST:
        agendamento_form = AgendamentoForm(request.POST)
        if agendamento_form.is_valid():
            agendamento = agendamento_form.save(commit=False)
            if passeio.vagas_disponiveis >= agendamento.quantidade_pessoas:
                agendamento.cliente = request.user
                agendamento.passeio = passeio
                passeio.vagas_disponiveis -= agendamento.quantidade_pessoas
                passeio.save()
                agendamento.save()
                messages.success(request, "Agendamento realizado com sucesso!")
                return redirect('meus_agendamentos')
            else:
                messages.error(request, f"Restam apenas {passeio.vagas_disponiveis} vagas.")

    # Avaliação
    if request.method == 'POST' and 'avaliar' in request.POST:
        avaliacao_form = AvaliacaoForm(request.POST)
        if avaliacao_form.is_valid():
            avaliacao = avaliacao_form.save(commit=False)
            avaliacao.usuario = request.user
            avaliacao.passeio = passeio
            avaliacao.save()
            messages.success(request, "Avaliação enviada!")
            return redirect('detalhe_passeio', passeio_id=passeio.id)

    return render(request, 'passeios/passeio_detalhe.html', {
        'passeio': passeio,
        'agendamento_form': agendamento_form,
        'avaliacao_form': avaliacao_form,
        'avaliacoes': passeio.avaliacoes.all().order_by('-data')
    })
    
def lista_passeios(request):
    passeios = Passeio.objects.all()
    form = PasseioForm(request.GET)

    if form.is_valid():
        data_min = form.cleaned_data.get('data_min')
        data_max = form.cleaned_data.get('data_max')
        preco_max = form.cleaned_data.get('preco_max')

        if data_min:
            passeios = passeios.filter(data__gte=data_min)
        if data_max:
            passeios = passeios.filter(data__lte=data_max)
        if preco_max:
            passeios = passeios.filter(preco__lte=preco_max)

    return render(request, 'passeios/lista.html', {
        'passeios': passeios,
        'form': form
    })

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


