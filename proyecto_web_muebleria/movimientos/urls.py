from django.urls import path

from . import views

app_name = 'movimientos'

urlpatterns = [
    path('home/', views.home, name='movimientos'),
    path('home/crearMovimiento/', views.crearMovimiento, name='crear_movimiento')
]