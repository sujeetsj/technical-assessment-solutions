from django.shortcuts import render
from .models import Order

def top_customers_view(request):
    top_customers = Order.get_top_5_customers()
    return render(request, 'top_customers.html', {'top_customers': top_customers})