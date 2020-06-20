from django.shortcuts import render
from products.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def do_search(request):
    product_list = Product.objects.filter(name__icontains=request.GET['q'])
    q = request.GET['q']
    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 12)
    total_products = product_list.count()
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "search_results.html", {"products": products,
                  "total_products": total_products, "q": q})


def search_by_class(request, stage):
    products = Product.objects.filter(stage=stage)
    return render(request, "search_results.html", {"products": products,
                                                   "stage": stage})


def search_by_class_subject(request, stage, subject):
    product_list = Product.objects.filter(stage=stage).filter(subject=subject)
    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 12)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "search_by_class_subject.html",
                  {"products": products,
                   "stage": stage, "subject": subject})
