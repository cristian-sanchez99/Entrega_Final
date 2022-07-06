from django.contrib import admin
from Autos.models import Autos
# Register your models here.
@admin.register(Autos)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name","price","SKU","active"] 
