from django.shortcuts import render, redirect

from .models import Movimiento

from ordenes.models import Orden

from elementos.models import Elementos

# Create your views here.

def home(request):
    movimiento = Movimiento.objects.all()
    orden = Orden.objects.all()
    elemento = Elementos.objects.all()
    return render(request, 'movimientos/home.html',{'movimiento':movimiento, 'orden':orden, 'elemento':elemento})

def crearMovimiento(request):
    cantidad = request.POST['numCantidad']
    valor_total = request.POST['numValor']
    id_orden = request.POST['idOrden']
    id_elemento = request.POST['idElemento']

    id_orden_obj = Orden.objects.get(pk=id_orden)
    id_elemento_obj = Elementos.objects.get(pk=id_elemento)
    
    movimiento = Movimiento.objects.create(cantidad = cantidad, valor_total = valor_total, id_orden = id_orden_obj, id_elemento = id_elemento_obj)

    return redirect('/movimientos/home')

def editarMovimiento(request, id):
    movimiento = Movimiento.objects.get(id = id)
    elemento = Elementos.objects.all()
    orden = Orden.objects.all()
    return render(request, 'movimientos/editarMovimiento.html', {'movimiento': movimiento, 'elemento': elemento, 'orden': orden})

def edicionMovimiento(request):
    id = request.POST['numId']
    cantidad = request.POST['numCantidad']
    valor_total = request.POST['numValor']
    id_orden = request.POST['idOrden']
    id_elemento = request.POST['idElemento']

    id_orden_obj = Orden.objects.get(pk=id_orden)
    id_elemento_obj = Elementos.objects.get(pk=id_elemento)
    movimiento = Movimiento.objects.get(id = id)
    movimiento.cantidad = cantidad
    movimiento.valor_total = valor_total
    movimiento.id_orden = id_orden_obj
    movimiento.id_elemento = id_elemento_obj
    movimiento.save()
    return redirect('/movimientos/home')


def eliminarMovimiento(request, id):
    movimiento = Movimiento.objects.get(id = id)
    movimiento.delete()
    return redirect('/movimientos/home')