
from django.urls import URLPattern, path

from . import views

urlpatterns:list[URLPattern] = [
    path('products' , views.ProductsView.as_view() , name='products') ,
    path('products/<int:id>/' , views.ProductView.as_view() , name='product') ,
]
