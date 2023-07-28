from django.contrib import admin

from .models import Categoria


# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('descripcion'),
    ordering = ['descripcion']


admin.site.register(Categoria, CategoriaAdmin)