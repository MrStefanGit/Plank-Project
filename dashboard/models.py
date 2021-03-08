from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

UNIT = (
    ('l', 'Liter'),
    ('cm', 'Centmieters'),
    ('pc', 'Piece'),
)

class ProductType(models.Model):
    product_type = models.CharField(max_length=10)

    def __str__(self):
        return self.product_type

class Products(models.Model):
    name = models.CharField(max_length=20)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    measurement = models.CharField(max_length=2, choices=UNIT, null=True)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Parteners(models.Model):
    name = models.CharField(max_length=20)
    registration_number = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    county = models.CharField(max_length=20)
    city = models.CharField(max_length=35)
    address = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    contact_person = models.CharField(max_length=35)
    manager = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Orders(models.Model):
    client = models.ForeignKey(Parteners, on_delete=models.DO_NOTHING)
    delivery_date = models.DateField(verbose_name='Delivery date')
    address = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)

class OrderDetails(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()

