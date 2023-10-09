from django.urls import path
from . import views

urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('crear/', views.crear_noticia, name='crear_noticia'),  # URL para crear noticias
    path('ver_noticias/', views.ver_noticias, name='ver_noticias'),  # Agrega esta línea
    path('noticias/eliminar/<int:noticia_id>/', views.eliminar_noticia, name='eliminar_noticia'),
]

