# Generated by Django 4.0.1 on 2022-06-01 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_producto_imgproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='microdetalleProducto',
            field=models.CharField(blank=True, max_length=1500, verbose_name='Detalle corto'),
        ),
    ]
