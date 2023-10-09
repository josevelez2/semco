from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia
from .forms import NoticiaForm

def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/noticias.html', {'noticias': noticias})

def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('noticias')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/crear_noticia.html', {'form': form})


def ver_noticias(request):
    # Recupera todas las noticias de la base de datos
    
    noticias = Noticia.objects.all()
    
    # Renderiza la página "ver_noticias.html" y pasa las noticias al contexto
    return render(request, 'noticias/ver_noticias.html', {'noticias': noticias})

def eliminar_noticia(request, noticia_id):
    # Obtén la noticia por su ID
    noticia = get_object_or_404(Noticia, pk=noticia_id)

    if request.method == 'POST':
        # Si se envió una solicitud POST, elimina la noticia
        noticia.delete()
        return redirect('ver_noticias')  # Redirige a la página de ver noticias o a donde desees

    return render(request, 'tu_template_ver_noticia.html', {'noticia': noticia})