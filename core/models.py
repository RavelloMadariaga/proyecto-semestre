from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name='ID Categoria')
    nombreCategoria = models.CharField(max_length=50,verbose_name="Nombre de la Categoria")
    rutaFoto = models.CharField(max_length=150,blank=True,verbose_name='RutaFoto')
    detalleCategoria = models.CharField(max_length=1500,blank=True,verbose_name='Detalle')

    def __str__(self):
        return self.nombreCategoria

class Colores(models.Model):
    idColor = models.AutoField(primary_key=True, verbose_name='ID Color')
    nombreColor = models.CharField(max_length=50,verbose_name="Nombre Color")

    def __str__(self):
        return self.nombreColor

#Modelo para Productos
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True,verbose_name="ID Produto")
    nombreProducto = models.CharField(max_length=20,verbose_name='Nombre Producto')
    imgProducto = models.CharField(max_length=500,null=True, blank=True,verbose_name='URL img')
    precioProducto = models.PositiveIntegerField(verbose_name='Precio')
    microdetalleProducto = models.CharField(max_length=1500,blank=True,verbose_name='Detalle corto')
    detalleProducto = models.CharField(max_length=1500,blank=True,verbose_name='Detalle')
    caracProducto = models.CharField(max_length=1500,blank=True,verbose_name='Caracteristicas')
    skuProducto = models.CharField(max_length=20,verbose_name='Sku')
    stockProducto = models.PositiveIntegerField(verbose_name='Stock')
    colorProducto = models.ForeignKey(Colores,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    retiroTienda = models.BooleanField(null=True, blank=True)
    despachoDomicilio = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.nombreProducto