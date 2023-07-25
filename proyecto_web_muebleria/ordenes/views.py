from django.shortcuts import render, redirect


from .models import Orden

from clientes.models import Cliente
# Create your views here.


def home(request):
    ordenes = Orden.objects.all()
    clientes = Cliente.objects.all()
    return render(request,'ordenes/home.html', {'ordenes':ordenes, 'clientes': clientes})

def crearOrden(request):

    fecha = request.POST['fecha']
    id_cliente = request.POST['idCliente']

    id_cliente_obj = Cliente.objects.get(pk=id_cliente)
    orden = Orden.objects.create(fecha = fecha, id_cliente = id_cliente_obj)
    return redirect('/ordenes/home')
    
def editarOrden(request, id):
    orden = Orden.objects.get(id = id)
    cliente = Cliente.objects.all()
    return render(request, 'ordenes/editarOrden.html', {'orden': orden, 'clientes':cliente})

def edicionOrden(request):
    id = request.POST['numId']
    fecha = request.POST['fecha']
    id_cliente = request.POST['idCliente']

    id_cliente_obj = Cliente.objects.get(pk=id_cliente)
    orden = Orden.objects.get(id = id)
    orden.fecha = fecha
    orden.id_cliente = id_cliente_obj
    orden.save()
    return redirect('/ordenes/home')

def eliminarOrden(request, id):
    orden = Orden.objects.get(id = id)
    orden.delete()
    return redirect('/ordenes/home')
