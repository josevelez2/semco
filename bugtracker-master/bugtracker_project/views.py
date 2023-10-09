from django.shortcuts import render

def home(request):
    # Tu lógica para la página de inicio aquí
    return render(request, 'index.html')

def compras(request):
    # Lógica para la página de compras
    return render(request, 'compras.html')

def direccion_tecnica(request):
    # Lógica para la página de dirección técnica
    return render(request, 'direccion_tecnica.html')

def noticias(request):
    # Lógica para la página de noticias
    return render(request, 'noticias.html')

def crear_app(request):
    # Lógica para la página de crear la app
    return render(request, 'crear_app.html')


