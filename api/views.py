from django import http
from django.http import Http404, HttpRequest
from django.shortcuts import render
from rest_framework.decorators import api_view as api
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


@api(['GET'])
def product_index(request:HttpRequest):
    if request.method == 'GET' :
        products = Product.objects.all()
        serializer = ProductSerializer(products , many=True)
        return Response(serializer.data)
    raise Http404()
