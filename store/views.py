from django.shortcuts import get_object_or_404, render
from .models import Product

def home(request):
    products = Product.objects.all()[:3]  # Mostramos los primeros 3 productos
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})
