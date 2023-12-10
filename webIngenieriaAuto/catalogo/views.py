from django.shortcuts import render
from .models import Product
# Create your views here.


def catalogo(request):
    listOfProducts = Product.objects.all()
    return render(request,"catalogo/catalogo.html", {'products': listOfProducts})