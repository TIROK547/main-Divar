from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, User
import json
# Create your views here.

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Product.objects.create(
            name = data.get("name"),
            price = data.get("price"),
            seller = User.objects.get(id=data.get("seller")),
        )
        return HttpResponse(f"product {data.get('name')} added")
    
def change_product_price(request):
    if request.method == "PATCH":
        data = json.loads(request.body)
        temp = Product.objects.get(data.id)
        temp.price = data.price
        temp.save()
        return HttpResponse(f"price changed to {data.get('price')}")
    
@csrf_exempt
def see_user_products(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        products = Product.objects.filter(seller=data.get("user_id"))
        product_list = [
            {"id": product.id, "name": product.name, "price": product.price}
            for product in products
            ]
        print(product_list)
        return JsonResponse(product_list,safe=False)
    
@csrf_exempt
def see_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        product_list = [
                {
                    "id": product.id,
                    "seller_id": product.seller.id,
                    "name": product.name,
                    "price": product.price,
                    "is_sold": product.is_sold
                }
                for product in products
            ]
        return JsonResponse(product_list,safe=False)
    
@csrf_exempt
def remove_product(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product = Product.objects.get(id=data.get("product_id"))
        product.delete()
        return HttpResponse("product deleted")