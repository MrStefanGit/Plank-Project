from django.urls import path, include
from . import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create/', users_views.create_user, name='create-user'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/homePage.html'), name='logout')
]

