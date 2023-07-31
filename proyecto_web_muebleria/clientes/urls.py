from django.urls import path
from . import views

app_name = 'clientes'
urlpatterns = [
    path('clientes/', views.home, name='clientes'),
    path('clientes/registrarCliente/', views.registrarCliente, name='registrar_cliente'),
    path('clientes/eliminarCliente/<id>/', views.eliminarCliente, name='eliminar_cliente'),
    path('clientes/editarCliente/<id>/', views.editarCliente, name='editar_cliente'),
    path('clientes/edicionCliente/', views.edicionCliente, name='edicion_cliente'),
    path('clientes/listarClientes/', views.listarClientes, name='listar_clientes')
]