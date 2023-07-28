from django.contrib import admin

from .models import Elementos
# Register your models here.


class ElementoAdmin(admin.ModelAdmin):
    ordering = ['descripcion']
    autocomplete_fields = ['id_categoria']

admin.site.register(Elementos, ElementoAdmin)

