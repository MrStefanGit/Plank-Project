# Generated by Django 3.0.4 on 2020-05-14 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_parteners'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttype',
            old_name='productType',
            new_name='product_type',
        ),
    ]
