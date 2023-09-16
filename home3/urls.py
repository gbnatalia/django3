from django.contrib import admin
from django.urls import path
from .views import OrderProductView, ListClientProducts
from .views import client, product, order

urlpatterns = [
    path('client/', client, name='client'),
    path('product/', product, name='product'),
    path('order/', order, name='order'),
    path('orders/<int:pk>', OrderProductView.as_view(), name='OrderProductView'),
    path('products/<int:pk>/<int:days>', ListClientProducts.as_view(), name='ListClientProducts'),
]