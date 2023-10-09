from django.contrib import admin
from .models import Page
from .models import Empleado,Hijo, Empresas_Temporales
from django.http import HttpResponse
from django.urls import path
from io import BytesIO
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }
        
admin.site.register(Empleado)
admin.site.register(Page, PageAdmin)
admin.site.register(Hijo)