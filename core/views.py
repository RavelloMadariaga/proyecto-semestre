from asyncio.windows_events import NULL
import re
from django.shortcuts import render, redirect
import pyparsing
from .models import Colores, Producto, Categoria, Postulacion
from django.db.models import Sum
import django_filters
from .forms import *


# Create your views here.

def home(request):
    return render(request, 'core/home.html',{'nbar':'inicio'})

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

def Postular(request):
    data = request.POST
    nombrePostulante=data['txtNombre']
    numeroPostulante=data['txtNumero']
    correoPostulante=data['txtCorreo']
    aboutPostulante=data['txtAbout']

    postula = Postulacion.objects.create(
        nombre=nombrePostulante,
        numero=numeroPostulante,
        correo=correoPostulante,
        about=aboutPostulante,
    )

    return redirect('/postulacion-exitosa')

def registrarProducto(request):
    optTiendaDomicilio = ''
    optDespacho = ''
    data = request.POST
    nombreProducto=data['txtNombre']
    imgProducto=data['txtUrlproducto']
    precioProducto=data['numPrecio']
    microdetalleProducto=data['txtDetalleCorto']
    detalleProducto=data['txtDetalle']
    caracProducto=data['txtCaracteristicas']
    skuProducto=data['numSku']
    stockProducto=data['numStock']
    colorProducto=data['txtColor']
    idCategoria=data['idCategoria']
    optTiendaDomicilio=data['RetiroTienda'] 
    optDespacho=data['Despacho']
    

    retiroTienda = False
    despachoDomicilio = False

    
    if optTiendaDomicilio == '1':
        retiroTienda = True
    else:   
        retiroTienda = False

    if optDespacho == '1':
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
    optTiendaDomicilio = ''
    optDespacho = ''
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
    optTiendaDomicilio=request.POST['RetiroTienda']
    optDespacho=request.POST['Despacho']

    retiroTienda = False
    despachoDomicilio = False


    if optTiendaDomicilio == '1':
        retiroTienda = True
    else:   
        retiroTienda = False

    if optDespacho == '1':
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
    nbar = ''

    CATID = request.GET.get('categoria')
    if CATID:
        productosListados = Producto.objects.filter(categoria=CATID)
        nbar = 'categorias'
    else:
        productosListados = Producto.objects.all() 
        nbar = 'productos'

    

    datos = {
        'productos': productosListados, 
        'categorias': categoriaLista,
    }

    return render(request, 'core/productos.html', {"datos":datos,'nbar':nbar})

def categorias(request):
    categoriaLista = Categoria.objects.all()
    return render(request, 'core/categorias.html', {'categorias':categoriaLista,'nbar':'categorias'})

def producto(request, idProducto):
    producto = Producto.objects.get(idProducto=idProducto)
    datos = {'producto' : producto}
    return render(request, "core/producto.html", {"datos":datos,'nbar':'productos'})

def categoria(request, cat_id):
    datos = Producto.objects.filter(categoria=cat_id)
    return render(request, "core/categoria.html", {"datos":datos})

def logeo(request):
    if request.user.is_authenticated:
        return redirect('../')
    else:
        return render(request,'core/sing-up.html')  

def checkout(request):
    return render(request,'core/check-out.html')

def fincompra(request):
    return render(request,'core/finalizado.html')

def terminos(request):
    return render(request,'core/terminos.html')

def postulacionexitosa(request):
    return render(request,'core/postulacion-exitosa.html')

def workwithus(request):
    return render(request,'core/workwithus.html')

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            # messages.success(request, f'Usuario {username} creado.')
            return redirect('../login/')
    else:
            form = UserRegisterForm()
        
    data = {'form': form}
    return render(request,"core/registro.html", data)

def paneladmin(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    colores = Colores.objects.all()
    postulacion = Postulacion.objects.all()
    
    return render(request,'core/admin/index.html', {'productos': productos,'categorias': categorias,'colores': colores,'postulacion': postulacion})

def paneluser(request):
    return render(request,'core/admin/userpanel.html')