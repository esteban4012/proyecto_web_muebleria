from django.urls import path

from .  import views

app_name = 'elementos'

urlpatterns = [
    path('home/', views.home, name='elementos'),
    path('home/crearElemento/', views.crearElemento, name='crear_elemento'),
    path('home/eliminarElemento/<id>/', views.eliminarElemento, name='eliminar_elemento'),
    path('home/editarElemento/<id>/', views.editarElemento, name='editar_elemento'),
    path('home/edicionElemento/', views.edicionElemento, name='edicion_elemento'),
    
]