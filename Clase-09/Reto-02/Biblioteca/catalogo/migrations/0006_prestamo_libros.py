# Generated by Django 2.2.2 on 2019-06-25 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_remove_prestamo_libros'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='libros',
            field=models.ManyToManyField(to='catalogo.Libro'),
        ),
    ]
