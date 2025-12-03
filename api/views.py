from django import http
from django.contrib.auth import get_user_model
from django.db import transaction
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status
from rest_framework.decorators import api_view as api
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer, RegistrationSerializer

User = get_user_model()


class ProductsView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer


class RegisterView2(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsView2(APIView):
    def get(self, request: Request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView2(APIView):
    def get(self, request: Request, id: int):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    def put(self, request: Request, id: int):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            with transaction.atomic():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, id: int):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            with transaction.atomic():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
