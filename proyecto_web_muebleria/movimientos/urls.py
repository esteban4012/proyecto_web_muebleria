from django.urls import path

from . import views

app_name = 'movimientos'

urlpatterns = [
    path('home/', views.home, name='movimientos'),
    path('home/crearMovimiento/', views.crearMovimiento, name='crear_movimiento'),
    path('home/eliminarMovimiento/<id>/', views.eliminarMovimiento, name='eliminar_movimiento'),
    path('home/editarMovimiento/<id>/', views.editarMovimiento, name='editar_movimiento'),
    path('home/edicionMovimiento/', views.edicionMovimiento, name='edicion_movimiento')
]