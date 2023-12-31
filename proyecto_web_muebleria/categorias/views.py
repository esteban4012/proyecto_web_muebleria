from django.shortcuts import render,redirect

from django.db.models import Q

from .models import Categoria

def home(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/home.html', {'categorias': categorias})

def crearCategoria(request):
    descripcion = request.POST['textDescripcion']
    categoria = Categoria.objects.create(descripcion = descripcion)
    return redirect('/categorias/home')

def editarCategoria(request, id):
    categoria = Categoria.objects.get(id = id)
    return render(request, 'categorias/editarCategoria.html', {'categoria': categoria})

def edicionCategoria(request):
    id = request.POST['numid']
    descripcion = request.POST['textDescripcion']
    categoria = Categoria.objects.get(id = id)
    categoria.descripcion = descripcion
    categoria.save()
    return redirect('/categorias/home')

def eliminarCategoria(request, id):
    categoria = Categoria.objects.get(id = id)
    categoria.delete()
    return redirect('/categorias/home')

def listarCategorias(request):
    
    busqueda = request.GET.get('buscar')

    if busqueda:
        categoria = Categoria.objects.filter(
            Q(descripcion__icontains = busqueda)
        ).distinct()
    else:
        categoria = Categoria.objects.all()
    return render(request,'categorias/home.html', {'categorias': categoria})