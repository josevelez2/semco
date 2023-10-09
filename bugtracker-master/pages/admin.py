from django.contrib import admin

from .models import Page, Empleado,Hijo, Empresas_Temporales
from django.http import HttpResponse
from django.urls import path
from io import BytesIO
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from .models import Empleado

def is_model_registered(model):
    """Returns True if the given model is registered, False otherwise."""
    for registered_model in admin.site._registry:
        if registered_model.__module__ == model.__module__ and registered_model.__name__ == model.__name__:
            return True
    return False

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'primer_nombre', 'primer_apellido', 'fecha_contratacion', 'de_quien_depende', 'empleado_activo')
    search_fields = ['cedula']


if not is_model_registered(Empleado):
    admin.site.register(Empleado, EmpleadoAdmin)

admin.site.register(Page, PageAdmin)
admin.site.register(Hijo)
