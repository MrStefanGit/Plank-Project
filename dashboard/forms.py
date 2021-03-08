from django.forms import ModelForm
from .models import Products, ProductType, Parteners, Orders, OrderDetails

class AddProductType(ModelForm):

    class Meta:
        model = ProductType
        fields = ('product_type',)

class AddProduct(ModelForm):

    class Meta:
        model = Products
        fields = ('name', 'product_type', 'measurement', 'quantity', 'price')

class AddPartener(ModelForm):

    class Meta:
        model = Parteners
        fields = ('name', 'registration_number', 'country', 'county', 'city', 'address', 'phone_number', 'email', 'contact_person', 'manager',)

class CreateOrder(ModelForm):

    class Meta:
        model = Orders
        fields = ('client', 'delivery_date', 'address', 'approved')

class AddOrderDetails(ModelForm):

    class Meta:
        model = OrderDetails
        fields = ('order', 'product', 'quantity')
