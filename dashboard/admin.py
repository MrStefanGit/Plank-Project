from django.contrib import admin
from .models import ProductType, Products, Parteners, Orders, OrderDetails

admin.site.register(ProductType)
admin.site.register(Products)
admin.site.register(Parteners)
admin.site.register(Orders)
admin.site.register(OrderDetails)

