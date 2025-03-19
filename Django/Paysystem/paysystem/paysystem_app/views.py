from django.shortcuts import render

from .models import Product

# Views


def index(request):
    products_lsit = Product.objects.all()
    context = {
        "product_list":products_lsit
    }
    return render(request, "paysystem_app/index.html", context)

def detail(request):
    detail_product = Product.objects.all()
    context = {
        "detail_product":detail_product
    }
    return render(request, "paysystem_app/detail.html", context)