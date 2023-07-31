from django.urls import path

from . import views

app_name = 'ordenes'

urlpatterns = [
    path('home/', views.home, name='ordenes'),
    path('home/crearOrden/', views.crearOrden, name='crear_orden'),
    path('home/eliminarOrden/<id>/', views.eliminarOrden, name='eliminar_orden'),
    path('home/editarOrden/<id>/', views.editarOrden, name='editar_orden'),
    path('home/edicionOrden/', views.edicionOrden, name='edicion_orden'),
    path('home/listarOrden/', views.listarOrdenes,name='listar_orden')
    
]