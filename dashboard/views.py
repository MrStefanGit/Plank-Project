from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from .models import Products, ProductType, Parteners, Orders, OrderDetails
from .forms import AddProduct, AddProductType, AddPartener, AddOrderDetails

# dashboard home view
@login_required
def dashboardHomePage(request):
    return render(request, 'dashboard/index.html', {})

@login_required
def dashboardUsersPage(request):
    context = {
        'users': CustomUser.objects.all()
    }
    return render(request, 'dashboard/users.html', context)

@login_required
def dashboardProductTypePage(request):
    context = {
        'productsTypes': ProductType.objects.all()
    }
    return render(request, 'dashboard/productType.html', context)

@login_required
def dashboardAddProductType(request):
    if request.method == 'POST':
        form = AddProductType(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #messages.succes(request, f'User created for {username}')
            return redirect('dashboard-product-type')
    else:
        form = AddProductType()
    return render(request, 'dashboard/addProductType.html', {'form': form})

@login_required
def productTypeUpdateView(request, id):
    context = {}
    obj = get_object_or_404(ProductType, id = id)
    form = AddProductType(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('dashboard-product-type')
    context['form'] = form
    return render(request, 'dashboard/addProductType.html', context)

@login_required
def dashboardProductsPage(request):
    context = {
        'products': Products.objects.all()
    }
    return render(request, 'dashboard/products.html', context)

@login_required
def dashboardAddProduct(request):
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #messages.succes(request, f'User created for {username}')
            return redirect('dashboard-products')
    else:
        form = AddProduct()
    return render(request, 'dashboard/addProduct.html', {'form': form})

@login_required
def productUpdateView(request, id):
    context = {}
    obj = get_object_or_404(Products, id = id)
    form = AddProduct(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('dashboard-products')
    context['form'] = form
    return render(request, 'dashboard/addProduct.html', context)

@login_required
def dashboardPartenersPage(request):
    context = {
        'parteners': Parteners.objects.all()
    }
    return render(request, 'dashboard/parteners.html', context)

@login_required
def dashboardAddPartener(request):
    if request.method == 'POST':
        form = AddPartener(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #messages.succes(request, f'User created for {username}')
            return redirect('dashboard-parteners')
    else:
        form = AddPartener()
    return render(request, 'dashboard/addPartener.html', {'form': form})

@login_required
def partenersDetailView(request, id):
    context = {}
    context['data'] = Parteners.objects.get(id = id)
    return render(request, 'dashboard/partenersDetailView.html', context)

@login_required
def partenersUpdateView(request, id):
    context = {}
    obj = get_object_or_404(Parteners, id = id)
    form = AddPartener(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('dashboard-parteners')
    context['form'] = form
    return render(request, 'dashboard/addPartener.html', context)


@login_required
def dashboardOrdersPage(request):
    context = {
        'orders': Orders.objects.all()
    }
    return render(request, 'dashboard/orders.html', context)

@login_required
def orderDetailView(request, id):
    context = {}
    context['data'] = Orders.objects.get(id = id)
    return render(request, 'dashboard/ordersDetailView.html', context)

@login_required
def dashboardAddOrderDetails(request, id):
    if request.method == 'POST':
        form = AddOrderDetails(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #messages.succes(request, f'User created for {username}')
            return redirect('orders-detail')
    else:
        form = AddPartener()
    return render(request, 'dashboard/addOrderDetails.html', {'form': form})
