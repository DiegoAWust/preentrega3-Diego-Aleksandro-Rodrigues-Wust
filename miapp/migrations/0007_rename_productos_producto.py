# Generated by Django 5.0.1 on 2024-02-07 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0006_productos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='productos',
            new_name='Producto',
        ),
    ]
