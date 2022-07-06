from django.urls import path
from Autos.views import automoviles,create_product,buscar_producto_view,detail_product_autos,delete_products,about_us

urlpatterns =[
    path("", automoviles, name = "automoviles"),
    path("create_product/", create_product, name = "create_product"),
    path("buscar_producto/",buscar_producto_view, name="buscar_producto"),
    path("about_us/",about_us, name="about_us"),
    path("detail_product_autos/<int:pk>/",detail_product_autos, name="detail_product_autos"),
    path("delete_products/<int:pk>/",delete_products, name="delete_products"),
    ] 
