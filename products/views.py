from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def product_info(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, "product-info.html", {'product': product})
