# Generated by Django 2.0.6 on 2018-11-26 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categorias',
        ),
        migrations.AddField(
            model_name='producto',
            name='categorias',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.categoriaProducto'),
        ),
    ]
