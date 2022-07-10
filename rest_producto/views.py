from itertools import product
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto
from .serializers import ProductoSerializer 
from  django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token


@csrf_exempt
@api_view(['GET', 'POST','PUT','DELETE'])

def lista_producto(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JSONParser().parse(request)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.isvalid():
            serializer.save()
            return Response(serializer.data)
        else:    
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
            producto.delete()
            return Response(serializer.errors, staus=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))
def detalle_producto(request, id):


    try:
        Producto = Producto.objects.get(idProducto = id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=ProductoSerializer(product)
        return Response (serializer.data)
    if request.method == 'PUT':
        data =JSONParser().parse(request)
        serializer=ProductoSerializer(product,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status-status.HTTP_204_NO_CONTENT)
