from asyncio.windows_events import NULL
import re
from django.shortcuts import render, redirect
import pyparsing
from .models import Colores, Producto, Categoria
from django.db.models import Sum
import django_filters

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def listadoproductos(request):

    productos = Producto.objects.all()

    datos = {
        'productos': productos
    }

    return render(request, 'core/productos.html', datos)

def mantenedor(request):

    productosListados = Producto.objects.all()
    categoriaLista = Categoria.objects.all()
    colorLista = Colores.objects.all()

    datos = {
        'productos': productosListados, 
        'categorias' :categoriaLista,
        'colorLista' : colorLista
    }

    return render(request, 'core/mantenedorProductos.html', {"datos":datos})

def registrarProducto(request):
    nombreProducto=request.POST['txtNombre']
    imgProducto=request.POST['txtUrlproducto']
    precioProducto=request.POST['numPrecio']
    microdetalleProducto=request.POST['txtDetalleCorto']
    detalleProducto=request.POST['txtDetalle']
    caracProducto=request.POST['txtCaracteristicas']
    skuProducto=request.POST['numSku']
    stockProducto=request.POST['numStock']
    colorProducto=request.POST['txtColor']
    idCategoria=request.POST['idCategoria']
    optDespacho=request.POST['opcionDespacho']
    optTiendaDomicilio=request.POST['opcionRetiro']
    

    retiroTienda = False
    despachoDomicilio = False

    
    if optTiendaDomicilio == 'opcionRetiro':
        retiroTienda = True
    else:
        retiroTienda = False

    if optDespacho == 'opcionDespacho':
        despachoDomicilio = True
    else:
         despachoDomicilio = False

    objCategoria = Categoria()
    objCategoria.idCategoria = int(idCategoria)

    objColor = Colores()
    objColor.idColor = int(colorProducto)

    producto = Producto.objects.create(
        nombreProducto=nombreProducto,
        imgProducto=imgProducto,
        precioProducto=precioProducto,
        microdetalleProducto=microdetalleProducto,
        detalleProducto=detalleProducto,
        caracProducto=caracProducto,
        skuProducto=skuProducto,
        stockProducto=stockProducto,
        colorProducto=objColor,
        categoria=objCategoria,
        retiroTienda=retiroTienda,
        despachoDomicilio=despachoDomicilio,
    )
    return redirect('/mascotasadmin/mantenedorProductos')


def edicionProducto(request, idProducto):

    producto = Producto.objects.get(idProducto=idProducto)
    categoriaLista = Categoria.objects.all()
    colorLista = Colores.objects.all()
    datos = {'producto' : producto, 'categoriaLista' : categoriaLista, 'colorLista' : colorLista}

    return render(request, "core/edicionProducto.html", {"datos":datos})

def editarProducto(request):
    idproducto=request.POST['idProducto']
    nombreProducto=request.POST['txtNombre']
    imgProducto=request.POST['txtUrlproducto']
    precioProducto=request.POST['numPrecio']
    microdetalleProducto=request.POST['txtDetalleCorto']
    detalleProducto=request.POST['txtDetalle']
    caracProducto=request.POST['txtCaracteristicas']
    skuProducto=request.POST['numSku']
    stockProducto=request.POST['numStock']
    idColor=request.POST['idColor']
    idCategoria=request.POST['idCategoria']
    optTiendaDomicilio=request.POST['opcionRetiro']
    optDespacho=request.POST['opcionDespacho']

    retiroTienda = False
    despachoDomicilio = False

    
    if optTiendaDomicilio == 'RetiroTienda':
        retiroTienda = True
    else:
        retiroTienda = False

    if optDespacho == 'DespachoDomicilio':
        despachoDomicilio = True
    else:
         despachoDomicilio = False

    objCategoria = Categoria()
    objCategoria.idCategoria = int(idCategoria)

    objColor = Colores()
    objColor.idColor = int(idColor)

    producto = Producto.objects.get(idProducto=idproducto)

    producto.nombreProducto=nombreProducto
    producto.imgProducto=imgProducto
    producto.precioProducto=precioProducto
    producto.microdetalleProducto=microdetalleProducto
    producto.detalleProducto=detalleProducto
    producto.caracProducto=caracProducto
    producto.skuProducto=skuProducto
    producto.stockProducto=stockProducto
    producto.colorProducto=objColor
    producto.categoria=objCategoria
    producto.retiroTienda=retiroTienda
    producto.despachoDomicilio=despachoDomicilio
    
    producto.save()
    return redirect('/mascotasadmin/mantenedorProductos')

def eliminarProducto(request,idProducto):
    producto = Producto.objects.get(idProducto=idProducto)
    producto.delete()
    return redirect('/mascotasadmin/mantenedorProductos')

##############################################################################################################


def listadoCategoria(request):

    categoria = Categoria.objects.all()

    datos = {
        'categoria': categoria
    }

    return render(request, 'core/mantenedorCategoria.html', {"datos":datos})


def registrarCategoria(request):
    nombreCategoria=request.POST['txtNombre']
    
    categoria = Categoria.objects.create(
        nombreCategoria=nombreCategoria,
        
    )
    return redirect('/mascotasadmin/mantenedorCategoria')

def eliminarCategoria(request,idCategoria):
    categoria = Categoria.objects.get(idCategoria=idCategoria)
    categoria.delete()
    return redirect('/mascotasadmin/mantenedorCategoria')

def edicionCategoria(request, idCategoria):

    categoria = Categoria.objects.get(idCategoria=idCategoria)
    datos = {'categoria' : categoria}

    return render(request, "core/edicionCategoria.html", {"datos":datos})

def editarCategoria(request):
    idCategoria=request.POST['idCategoria']
    nombreCategoria=request.POST['txtNombre']

    categoria = Categoria.objects.get(idCategoria=idCategoria)

    categoria.nombreCategoria=nombreCategoria
    categoria.save()
    return redirect('/mascotasadmin/mantenedorCategoria')

##############################################################################################################

def productos(request):
    categoriaLista = Categoria.objects.all()

    CATID = request.GET.get('categoria')
    if CATID:
        productosListados = Producto.objects.filter(categoria=CATID)
    else:
        productosListados = Producto.objects.all() 

    datos = {
        'productos': productosListados, 
        'categorias': categoriaLista
    }

    return render(request, 'core/productos.html', {"datos":datos})

def categorias(request):
    categoriaLista = Categoria.objects.all()
    return render(request, 'core/categorias.html', {'categorias':categoriaLista})

def producto(request, idProducto):
    producto = Producto.objects.get(idProducto=idProducto)
    datos = {'producto' : producto}
    return render(request, "core/producto.html", {"datos":datos})

def categoria(request, cat_id):
    datos = Producto.objects.filter(categoria=cat_id)
    return render(request, "core/categoria.html", {"datos":datos})

def logeo(request):
    return render(request,'core/sing-up.html')

def checkout(request):
    return render(request,'core/check-out.html')

def fincompra(request):
    return render(request,'core/finalizado.html')

def paneladmin(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    colores = Colores.objects.all()
    
    return render(request,'core/admin/index.html', {'productos': productos,'categorias': categorias,'colores': colores})