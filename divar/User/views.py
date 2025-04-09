from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import User
import json

# Create your views here.

@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        User.objects.create(
            name=data.get("name"),
            last_name=data.get("last_name"),
            phone_number=data.get("phone_number"),
        )
        return HttpResponse(f"User '{data.get('name')}' created")
    
@csrf_exempt
def update_user_name(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get("user_id")
        new_name = data.get("name")
        temp = User.objects.get(id=user_id)
        temp.name = new_name
        temp.save()
        return HttpResponse(f"Name changed to {new_name}")
