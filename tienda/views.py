from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

def inicio(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    categoria_id = request.GET.get('categoria')
    seleccionar = request.GET.get('seleccionar')

    if categoria_id:
        productos = productos.filter(categoria_id = categoria_id)

    if seleccionar:
        productos = productos.filter(nombre_icontains=seleccionar)

    return render(request, 'tienda/inicio.html', {
        'productos' : productos,
        'categorias' : categorias,

    })

def detalle(request, id):
    producto = get_object_or_404(Producto, id = id)
    return render(request, 'tienda/detalle.html', {'producto': producto})

    

