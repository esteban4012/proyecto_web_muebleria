from django.shortcuts import render,redirect

from .models import Cliente

# Create your views here.

def home(request):
    cliente = Cliente.objects.all()
    return render(request,'clientes/home.html',{"cliente" : cliente})


def registrarCliente(request):
    
    nombre = request.POST['textNombre']
    apellido = request.POST['textApellido']
    apellido_2 = request.POST['textApellido2']
    numero_identificacion = request.POST['numId']
    direccion = request.POST['textDireccion']
    telefono = request.POST['numTelefono']
    correo = request.POST['textCorreo']

    cliente = Cliente.objects.create(nombre = nombre, apellido = apellido, apellido_2 = apellido_2, numero_identificacion = numero_identificacion , direccion = direccion, telefono = telefono, correo = correo)

    return redirect('/clientes/clientes')

def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id = id)
    cliente.delete()
    return redirect('/clientes/clientes')

def editarCliente(request, id):
    cliente = Cliente.objects.get(id = id)
    return render(request,'clientes/editarCliente.html',{'cliente': cliente})

def edicionCliente(request):
    id = request.POST['numid']
    nombre = request.POST['textNombre']
    apellido = request.POST['textApellido']
    apellido_2 = request.POST['textApellido2']
    numero_identificacion = request.POST['numId']
    direccion = request.POST['textDireccion']
    telefono = request.POST['numTelefono']
    correo = request.POST['textCorreo']

    cliente = Cliente.objects.get(id = id)

    cliente.nombre = nombre
    cliente.apellido = apellido
    cliente.apellido_2 = apellido_2
    cliente.numero_identificacion = numero_identificacion
    cliente.direccion = direccion
    cliente.telefono = telefono
    cliente.correo = correo

    cliente.save()
    return redirect('/clientes/clientes')




