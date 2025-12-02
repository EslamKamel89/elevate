
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Product

User = get_user_model()

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta :
        model = Product
        fields = ["id" ,"name" ,"description" ,"price" ,"created_at" ,"updated_at"  ]

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type' : 'password'} ,
        write_only=True ,
        trim_whitespace=False
        )
    password2 = serializers.CharField(
        style={'input_type':'password'},
        write_only=True ,
        trim_whitespace=False ,
        label='Confirm Password'
        )
    username= serializers.CharField(
        required=True ,
        validators = [UniqueValidator(queryset=User.objects.all() ,  message="A user with that username already exists.")]
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message="A user with that email already exists.")]
    )
    class Meta :
        model = User
        fields = ['username','first_name' ,'last_name' ,'email' ,'password' , 'password2']
        extra_kwargs = {
            'password' : {'write_only':True} ,
            'password2' : {'write_only':True} ,
            'email' : {'required':True} ,
        }


    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2 :
            raise serializers.ValidationError({'password':"passwords do not match"})
        try:
            validate_password(password , user=None)
        except ValidationError as e:
            raise serializers.ValidationError({'password' : list(e.messages)})
        return super().validate(attrs)

    def create(self, validated_data:dict):
        validated_data = validated_data.copy()
        validated_data.pop('password2' , None)
        password = validated_data.pop('password')
        try:
            with transaction.atomic():
                user = User(**validated_data)
                user.set_password(password)
                user.save()
        except IntegrityError as e:
            raise serializers.ValidationError({"detail": "User could not be created. Integrity error."})
        return user

