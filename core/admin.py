from django.contrib import admin
from .models import Categoria, Producto, Colores
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
     list_display=('idCategoria','nombreCategoria', 'detalleCategoria','rutaFoto')
admin.site.register(Categoria, CategoriaAdmin)

class ColoresAdmin(admin.ModelAdmin):
     list_display=('idColor','nombreColor')
admin.site.register(Colores, ColoresAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display=('idProducto', 'nombreProducto', 'precioProducto','stockProducto','categoria','colorProducto','retiroTienda','despachoDomicilio')
admin.site.register(Producto, ProductoAdmin)
