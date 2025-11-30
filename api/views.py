from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


def product_list(request:HttpRequest):
    pass
