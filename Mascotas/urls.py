"""Mascotas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Mascotas import views
from Mascotas.viewslogin import login
from core.views import lista_producto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('/', include('rest_productos')),
    path('lista_productos',views.lista_producto,name="lista_productos"),
    path('detalle_producto/‹id›',views.detalle_producto,name="detalle_producto"),
    path('login', login, name="login"),
    ]
