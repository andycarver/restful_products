from django.shortcuts import render, HttpResponse, redirect
from models import Product
  # Create your views here.
def index(request):
    context={
    'products':Product.objects.all()[::-1]

    }
    return render(request, "products/index.html", context)

def show(request):
    pass

def new(request):
    return render(request, "products/new.html")

def edit(request, id):
    return render(request, "products/edit.html")

def create(request):
    Product.objects.create_new_product(request)
    return redirect("products:index")

def update(request):
    pass

def destroy(request):
    pass
