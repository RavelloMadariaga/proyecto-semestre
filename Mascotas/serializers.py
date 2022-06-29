from rest_framework import serializers
from core.models import Producto


class ProductoSerializer(serializers.ModelsSerielizer):
    class Meta:
        model = Producto
        fields=['','','','']#aniadir productos


