from django.urls import path
from .views import add_product,see_user_products,see_products,remove_product
urlpatterns =[
    path("add-product",add_product),
    path("see-user-product",see_user_products),
    path("see-products",see_products),
    path("delete-product",remove_product),
]
