from django.shortcuts import render

def direccion_tecnica(request):
    # Lógica específica de la opción de Dirección Técnica aquí
    return render(request, 'direccion_tecnica/direccion_tecnica.html', {})
