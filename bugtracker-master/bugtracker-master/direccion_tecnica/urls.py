from django.urls import path
from . import views

urlpatterns = [
    path('', views.direccion_tecnica, name='direccion_tecnica'),  # URL para la opción de Dirección Técnica
]