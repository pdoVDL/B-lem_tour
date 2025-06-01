from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('passeios/', include('passeios.urls')),
    path('agendamentos/', include('agendamentos.urls')),
]
