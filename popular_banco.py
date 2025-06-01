from passeios.models import Passeio
from datetime import date

Passeio.objects.create(
    titulo="Centro Histórico de Belém",
    descricao="Visita ao Ver-o-Peso, Forte do Presépio, Catedral e ruas coloniais.",
    local="Centro de Belém",
    data=date(2025, 11, 22),
    preco=60.00
)

Passeio.objects.create(
    titulo="Belém Panorâmico",
    descricao="Tour guiado de van pelos principais pontos turísticos.",
    local="Belém",
    data=date(2025, 11, 23),
    preco=75.00
)

Passeio.objects.create(
    titulo="Mangal das Garças",
    descricao="Trilha, mirante e borboletário.",
    local="Mangal das Garças",
    data=date(2025, 11, 24),
    preco=50.00
)

Passeio.objects.create(
    titulo="Ilha do Combu",
    descricao="Passeio de barco, visita ao chocolate artesanal e floresta de várzea.",
    local="Ilha do Combu",
    data=date(2025, 11, 25),
    preco=80.00
)

Passeio.objects.create(
    titulo="Feira do Ver-o-Peso + Degustação",
    descricao="Visita guiada ao mercado com degustação de frutas, peixes e temperos regionais.",
    local="Ver-o-Peso",
    data=date(2025, 11, 26),
    preco=45.00
)

Passeio.objects.create(
    titulo="Rota do Tacacá e Maniçoba",
    descricao="Degustação de pratos típicos em restaurantes locais.",
    local="Belém - Restaurantes",
    data=date(2025, 11, 27),
    preco=70.00
)

Passeio.objects.create(
    titulo="Furo do Benedito (Barco)",
    descricao="Navegação entre igarapés e mata de várzea com guia local.",
    local="Furo do Benedito",
    data=date(2025, 11, 28),
    preco=90.00
)

Passeio.objects.create(
    titulo="Pôr do Sol na Baía do Guajará",
    descricao="Passeio ao entardecer com música ao vivo.",
    local="Baía do Guajará",
    data=date(2025, 11, 29),
    preco=85.00
)

print("Passeios cadastrados com sucesso!")
