from django.contrib import admin
from .models import Categoria
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria')
    list_display_links = ('id', 'nome_categoria')

admin.site.register(Categoria, CategoriaAdmin)
