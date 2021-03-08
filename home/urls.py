from django.urls import path, include
from . import views as home_views

urlpatterns = [
    # path to home page
    path('', home_views.homePage, name='home-page'),
]
