
from django.urls import URLPattern, path

from . import views

urlpatterns:list[URLPattern] = [
    path('products' , views.ProductView.as_view() , name='products.index') ,
]
