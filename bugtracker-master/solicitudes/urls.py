from django.urls import path
from . import views

urlpatterns = [
    path('', views.solicitudes, name='solicitudes'),
    # Otras URLs de la aplicación 'solicitudes' si las tienes
]