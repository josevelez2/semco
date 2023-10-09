from django.urls import path
from . import views

urlpatterns = [
    path('', views.compras, name='compras'),  # URL para la opción de Compras
]