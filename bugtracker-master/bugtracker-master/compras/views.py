from django.shortcuts import render

def compras(request):
    # Lógica específica de la opción de Compras aquí
    productos = ["Producto 1", "Producto 2", "Producto 3"]
    return render(request, 'compras/compras.html', {'productos': productos})
