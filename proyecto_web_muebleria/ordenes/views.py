from django.shortcuts import render, redirect

from .models import Orden

from clientes.models import Cliente

from elementos.models import Elementos

# Create your views here.


def home(request):
    ordenes = Orden.objects.all()
    clientes = Cliente.objects.all()
    elementos = Elementos.objects.all()
    return render(request,'ordenes/home.html', {'ordenes':ordenes, 'clientes': clientes, 'elemento': elementos})

def crearOrden(request):

    fecha = request.POST['fecha']
    cantidad = request.POST['numCantidad']
    valor_total = request.POST['numValor']
    id_elemento = request.POST['idElemento']
    id_cliente = request.POST['idCliente']

    id_elemento_obj = Elementos.objects.get(pk=id_elemento)
    id_cliente_obj = Cliente.objects.get(pk=id_cliente)
    orden = Orden.objects.create(fecha = fecha,cantidad = cantidad, valor_total = valor_total, id_elemento = id_elemento_obj, id_cliente = id_cliente_obj)
    return redirect('/ordenes/home')
    
def editarOrden(request, id):
    orden = Orden.objects.get(id = id)
    cliente = Cliente.objects.all()
    elemento = Elementos.objects.all()
    return render(request, 'ordenes/editarOrden.html', {'orden': orden, 'clientes':cliente, 'elemento':elemento})

def edicionOrden(request):
    id = request.POST['numId']
    fecha = request.POST['fecha']
    cantidad = request.POST['numCantidad']
    valor_total = request.POST['numValor']
    id_elemento = request.POST['idElemento']
    id_cliente = request.POST['idCliente']
    id_elemento_obj = Elementos.objects.get(pk=id_elemento)
    id_cliente_obj = Cliente.objects.get(pk=id_cliente)
    orden = Orden.objects.get(id = id)
    orden.fecha = fecha
    orden.cantidad = cantidad
    orden.valor_total = valor_total
    orden.id_elemento = id_elemento_obj
    orden.id_cliente = id_cliente_obj
    orden.save()
    return redirect('/ordenes/home')

def eliminarOrden(request, id):
    orden = Orden.objects.get(id = id)
    orden.delete()
    return redirect('/ordenes/home')
