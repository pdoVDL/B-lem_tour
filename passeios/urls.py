from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_passeios, name='lista_passeios'),
    path('novo/', views.criar_passeio, name='criar_passeio'),
    path('<int:pk>/editar/', views.editar_passeio, name='editar_passeio'),
    path('<int:pk>/excluir/', views.excluir_passeio, name='excluir_passeio'),
    path('<int:passeio_id>/', views.agendar_passeio, name='agendar_passeio'),
]
