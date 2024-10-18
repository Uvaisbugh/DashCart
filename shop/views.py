from django.shortcuts import get_object_or_404, render
from . models import category,Product
from django.core.paginator import  Paginator,EmptyPage,InvalidPage

# Create your views here.

# def index(request):
#     return render(request,'index.html')

def allprodcat(request, c_slug=None):
    c_page = None
    products_list = None

    if c_slug:
        c_page = get_object_or_404(category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.filter(available=True)

    paginator = Paginator(products_list, 6)
    page = request.GET.get('page', 1)

    try:
        products = paginator.page(page)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)  # Return last page
    except InvalidPage:
        products = paginator.page(1)  # Return first page in case of an invalid request

    return render(request, 'category.html', {'category': c_page, 'products': products})

def ProDetail(request, c_slug, product_slug):
    product = get_object_or_404(Product, category__slug=c_slug, slug=product_slug)
    return render(request, 'product.html', {'product': product})
