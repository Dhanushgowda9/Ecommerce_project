from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
import csv


# 1. CSV export view
def export_orders_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'
    writer = csv.writer(response)
    writer.writerow(['Order ID', 'Customer', 'Email', 'Product', 'Quantity', 'Total', 'Status', 'Date'])

    orders = Order.objects.all()
    for order in orders:
        writer.writerow([
            order.id,
            order.customer_name,
            order.email,
            order.product.name,
            order.quantity,
            order.total_price,
            order.status,
            order.created_at
        ])
    return response


# 2. Home page — show all products
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


# 3. Order form — one product
def order_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        quantity = int(request.POST['quantity'])
        total = product.price * quantity

        Order.objects.create(
            customer_name=name,
            email=email,
            product=product,
            quantity=quantity,
            total_price=total
        )
        return redirect('order_success')

    return render(request, 'order.html', {'product': product})


# 4. Success page
def order_success(request):
    return render(request, 'success.html')

