from django.shortcuts import render

def solicitudes(request):
    # Tu lógica de vista aquí
    return render(request, 'noticias/solicitudes.html', {'solicitudes': solicitudes})
from django.shortcuts import render

def solicitudes_view(request):
    # Tu lógica de vista aquí
    return render(request, 'solicitudes/solicitudes.html')
