
from django.urls import URLPattern, path

from . import views

urlpatterns:list[URLPattern] = [
    path('products' , views.product_index , name='products.index') ,
]
