# Generated by Django 3.0.4 on 2020-05-14 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20200515_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parteners',
            old_name='contactPerson',
            new_name='contact_person',
        ),
        migrations.RenameField(
            model_name='parteners',
            old_name='phoneNumber',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='parteners',
            old_name='registrationNr',
            new_name='registration_number',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='productType',
            new_name='product_type',
        ),
    ]