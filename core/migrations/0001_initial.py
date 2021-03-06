# Generated by Django 4.0.1 on 2022-05-31 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Produto')),
                ('nombreProducto', models.CharField(max_length=20, verbose_name='Nombre Producto')),
                ('precioProducto', models.PositiveIntegerField(verbose_name='Precio')),
                ('detalleProducto', models.CharField(blank=True, max_length=1500, verbose_name='Detalle')),
                ('caracProducto', models.CharField(blank=True, max_length=1500, verbose_name='Caracteristicas')),
                ('skuProducto', models.CharField(max_length=20, verbose_name='Sku')),
                ('stockProducto', models.PositiveIntegerField(verbose_name='Stock')),
                ('colorProducto', models.CharField(blank=True, max_length=20, null=True, verbose_name='Color')),
                ('retiroTienda', models.BooleanField(blank=True, null=True)),
                ('despachoDomicilio', models.BooleanField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
