from multiprocessing import context
from urllib import request
from django.shortcuts import render
from Autos.models import Autos
from Autos.forms import Autos_forms
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from django.views.generic import ListView 
# Create your views here.


def automoviles(request):
    autos = Autos.objects.all()
    context = {"autos":autos}
    return render(request,"automoviles.html", context=context)

def about_us(request):
    message = "Somos la empresa que tiene el auto de tus sueños. Nos encargamos de traer los autos de mejor y mas alta gama en el mercado"
    context = {"message":message}
    return render(request,"about_us.html", context=context)

@login_required
def create_product(request):
    if request.method == "GET":
        form = Autos_forms()
        context = {"form":form}
        return render(request,"create_product.html",context = context)
    else:
        form = Autos_forms(request.POST)
        if form.is_valid():
            new_product = Autos.objects.create(
                name = form.cleaned_data["name"],
                price = form.cleaned_data["price"],
                description = form.cleaned_data["description"],
                SKU = form.cleaned_data["SKU"],
                active = form.cleaned_data["active"],
            )
            context={"new_product":new_product}
        return render(request,"create_product.html",context = context)


def buscar_producto_view(request):
    productos = Autos.objects.filter(name__icontains = request.GET["search"])
    context = {"productos":productos}
    return render(request,"buscar_productos.html",context=context)


def detail_product_autos(request,pk):
    try:
        product = Autos.objects.get(id=pk)
        context = {"product":product}
        return render(request,"detail_product.html",context = context)
    except:
        context = ("Error: El producto no existe")
        return render(request,"automoviles.html", context=context)


@login_required
def delete_products(request,pk):
    try:   
        if request.method == "GET":
            product = Autos.objects.get(id=pk)
            context = {"product":product}
            return render(request,"delete_products.html", context=context)
        else:
            product = Autos.objects.get(id=pk)
            product.delete()
            context = {"message":"el producto fue eliminado"}
            return render(request,"automoviles.html", context=context)
    except:
            context = {"Error: El producto no existe"}
            return render(request,"automoviles.html", context=context)