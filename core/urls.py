from django.urls import path, include 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import *
from .views import *
from .forms import *
from django.contrib.auth.views import LoginView, LogoutView
#from Mascotas.core import views
from . import views

urlpatterns = [
    path('', home,name="home"),
    #Main web
    path('postular/',views.Postular),
    path('productos',views.productos),
    path('categorias',views.categorias),
    path('producto/<idProducto>',views.producto),
    path('categoria/<cat_id>',views.categoria),
    path('check-out',views.checkout),
    path('fin-compra',views.fincompra),
    path('workwithus',views.workwithus),
    path('terminos',views.terminos),
    path('postulacion-exitosa',views.postulacionexitosa),
    #admin
    path('mascotasadmin/panel',views.paneladmin),
    path('mascotasadmin/mantenedorProductos',mantenedor, name="mantenedorProductos"),
    path('mascotasadmin/mantenedorCategoria',views.listadoCategoria),
    path('mascotasadmin/registrarProducto/',views.registrarProducto),
    path('mascotasadmin/edicionProducto/<idProducto>', views.edicionProducto),
    path('mascotasadmin/editarProducto/',views.editarProducto),
    path('mascotasadmin/eliminarProducto/<idProducto>', views.eliminarProducto),
    path('mascotasadmin/registrarCategoria/',views.registrarCategoria),
    path('mascotasadmin/eliminarCategoria/<idCategoria>', views.eliminarCategoria),
    path('mascotasadmin/edicionCategoria/<idCategoria>', views.edicionCategoria),
    path('mascotasadmin/editarCategoria/',views.editarCategoria),
    #Usuario
    path('login/', LoginView.as_view(template_name ='core\login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name ='core\logout.html'), name='logout'),
    path('registro/',views.registro),
    path('mi_cuenta/panel',views.paneluser),

   path('lista_productos', lista_producto, name='lista_productos'),
]


