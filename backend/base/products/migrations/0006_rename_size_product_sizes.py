# Generated by Django 5.1 on 2024-11-01 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_sex'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='size',
            new_name='sizes',
        ),
    ]