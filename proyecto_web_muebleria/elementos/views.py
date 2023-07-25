from django.shortcuts import render, redirect

from .models import Elementos,Categoria

# Create your views here.

def home(request):
    elementos = Elementos.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'elementos/home.html', {'elementos': elementos, 'categorias': categorias})

def crearElemento(request):
    
    descripcion = request.POST['textDescripcion']
    precio = request.POST['numPrecio']
    id_categoria = request.POST['textCategoria']

    try:
        categoria_obj = Categoria.objects.get(pk=id_categoria)
        elemento = Elementos(descripcion=descripcion, precio=precio, id_categoria=categoria_obj)
        elemento.save()
        return redirect('/elementos/home')
    except Categoria.DoesNotExist:
        # Manejo de error en caso de que la categoría no exista
        pass

def editarElemento(request, id):
    elemento = Elementos.objects.get(id = id)
    categoria = Categoria.objects.all()
    return render(request, 'elementos/editarElemento.html', {'elemento': elemento, 'categorias' : categoria})

def edicionElemento(request):
    id = request.POST['numId']
    descripcion = request.POST['textDescripcion']
    precio = request.POST['numPrecio']
    id_categoria = request.POST['textCategoria']
    categoria_obj = Categoria.objects.get(pk=id_categoria)
    elemento = Elementos.objects.get(id = id)

    elemento.descripcion = descripcion
    elemento.precio = precio
    elemento.id_categoria = categoria_obj
    elemento.save()
    return redirect('/elementos/home')



def eliminarElemento(request, id):
    elemento = Elementos.objects.get(id = id)
    elemento.delete()
    return redirect('/elementos/home')