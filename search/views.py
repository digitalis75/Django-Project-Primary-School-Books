from django.shortcuts import render
from products.models import Product


# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "search_results.html", {"products": products})


def search_by_class(request, stage):
    products = Product.objects.filter(stage=stage)
    return render(request, "search_results.html", {"products": products, "stage": stage})
