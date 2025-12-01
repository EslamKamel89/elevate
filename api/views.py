from django import http
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view as api
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


class ProductView(APIView):
    def get(self ,request:Request):
        products = Product.objects.all()
        serializer = ProductSerializer(products , many=True)
        return Response(serializer.data)
    def post(self , request:Request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


