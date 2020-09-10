from django.urls import path

from . import views

urlpatterns = [
    # path('foodpage/', views.Food, name='Food'),
    # path('cart/', views.Cart, name='Cart'),
    # path('search/', views.Search, name='Search'),
    # path('login/', views.Login, name='Login'),
    # path('logout/', views.Logout, name='Logout'),
    # path('register/', views.Register, name='Register'),
    path('', views.index, name='index')
]