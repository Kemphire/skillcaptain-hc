from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from datetime import date, timedelta

from .models import Product


def product_retrive_by_price_in_descending(request):
    all_prods = Product.objects.all().order_by("-price")
    data = serializers.serialize("json", all_prods)
    return JsonResponse(data, safe=False)


def product_retrive_by_specific_price_range(request):
    prods = Product.objects.filter(price__gte=5000, price__lte=7000)
    data = [
        {
            "name": prod.name,
            "price": prod.price,
            "description": prod.description,
            "category": prod.category,
            "created_at": prod.created_at,
        }
        for prod in prods
    ]
    return JsonResponse(data, safe=False)


def product_added_withing_seven_days(request):
    prods = Product.objects.filter(
        created_at__lte=date.today(), created_at__gte=date.today() - timedelta(days=7)
    )
    data = serializers.serialize("json", prods)
    return JsonResponse(data, safe=False)


def products_containing_skill(request):
    prods = Product.objects.filter(name__contains="skill")
    data = serializers.serialize("json", prods)
    return JsonResponse(data, safe=False)
