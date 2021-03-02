from django.shortcuts import render
from .models import Item


def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home.html", context)


def checkout(request):
    return render(request, "checkout.html")


def products(request):
    return render(request, "products.html")
