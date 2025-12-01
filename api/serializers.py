from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta :
        model = Product
        fields = ["id" ,"name" ,"description" ,"price" ,"created_at" ,"updated_at"  ]
