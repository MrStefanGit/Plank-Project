from django.urls import path, include
from . import views as dashboard_views

urlpatterns = [
    path('home/', dashboard_views.dashboardHomePage, name='dashboard-home'),

    path('users/', dashboard_views.dashboardUsersPage, name='dashboard-users'),

    path('producttype/', dashboard_views.dashboardProductTypePage, name='dashboard-product-type'),
    path('producttype/add/', dashboard_views.dashboardAddProductType, name='add-product-type'),
    path('producttype/<id>/update/', dashboard_views.productTypeUpdateView, name='product-type-update'),

    path('products/', dashboard_views.dashboardProductsPage, name='dashboard-products'),
    path('products/add/', dashboard_views.dashboardAddProduct, name='add-product'),
    path('products/<id>/update/', dashboard_views.productUpdateView, name='product-update'),

    path('parteners/', dashboard_views.dashboardPartenersPage, name='dashboard-parteners'),
    path('parteners/add/', dashboard_views.dashboardAddPartener, name='add-partener'),
    path('parteners/<id>/', dashboard_views.partenersDetailView, name='parteners-detail'),
    path('parteners/<id>/update/', dashboard_views.partenersUpdateView, name='parteners-update'),

    path('orders/', dashboard_views.dashboardOrdersPage, name='dashboard-orders'),
    path('orders/<id>/', dashboard_views.orderDetailView, name='orders-detail'),
    path('orders/<id>/addproduct/', dashboard_views.dashboardAddOrderDetails, name='orders-detail-add'),
]
