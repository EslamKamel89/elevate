from django.contrib import admin

from api.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name' , 'description' , 'price',)
    list_search = ('name',)

admin.site.register(Product , ProductAdmin)
