from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.order_product, name='order_product'),
    path('success/', views.order_success, name='order_success'),
    path('export-orders/', views.export_orders_csv, name='export_orders'),
]
