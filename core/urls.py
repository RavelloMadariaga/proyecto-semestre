from django.urls import path
from .views import home, listadoproductos, logeo, mantenedor, productos
#from Mascotas.core import views
from . import views

urlpatterns = [
    path('', home,name="home"),
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
    path('productos',views.productos),
    path('categorias',views.categorias),
    path('producto/<idProducto>',views.producto),
    path('categoria/<cat_id>',views.categoria),
    path('log-in',views.logeo),
    path('check-out',views.checkout),
    path('fin-compra',views.fincompra),
]