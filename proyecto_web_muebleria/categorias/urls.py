from django.urls import path

from . import views

app_name = 'categorias'

urlpatterns = [
    path('home/',views.home, name='categorias'),
    path('home/crearCategoria/', views.crearCategoria, name='crear_categoria'),
    path('home/eleminarCategoria/<id>/', views.eliminarCategoria,name='eliminar_categoria'),
    path('home/editarCategoria/<id>/', views.editarCategoria, name='editar_categoria'),
    path('home/edicionCategoria/', views.edicionCategoria,name='edicion_categoria'),
    path('home/listarCategoria/', views.listarCategorias, name='listar_categorias')
]