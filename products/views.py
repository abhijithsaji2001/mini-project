from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from .models import Product
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return  render(request, "homepage.html")

def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "product_list.html", { "page_obj": page_obj })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_details.html", {"product": product})

def search_product(request):
    query = request.GET.get("search_bar")  # get search input
    if query:
        products = Product.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()

    return render(request, "product_search.html", {"products": products})

def product_shoes(request):
    products = Product.objects.filter( product_type = 'shoes')
    return render(request, "product_search.html", {"products": products})

def product_grocery(request):
    products = Product.objects.filter( product_type = 'grocery')
    return render(request, "product_search.html", {"products": products})

def product_cosmetics(request):
    products = Product.objects.filter( product_type = 'cosmetics')
    return render(request, "product_search.html", {"products": products})

def product_dress(request):
    products = Product.objects.filter( product_type = 'dress')
    return render(request, "product_search.html", {"products": products})