from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_agendamentos, name='lista_agendamentos'),
    path('<int:pk>/editar/', views.editar_agendamento, name='editar_agendamento'),
    path('<int:pk>/excluir/', views.excluir_agendamento, name='excluir_agendamento'),
    path('criar/<int:passeio_id>/', views.criar_agendamento_com_passeio, name='criar_agendamento_com_passeio'),
    path('meus/', views.meus_agendamentos, name='meus_agendamentos'),
]
