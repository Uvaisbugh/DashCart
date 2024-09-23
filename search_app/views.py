from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def searchResults(request):
  product=None
  query=None
  if 'q' in request.GET:
      query=request.GET.get('q')
      product=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
      return render(request,'search.html',{'query':query,'products':product})