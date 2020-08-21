from django.contrib import admin

from shop.models.category import Category
from shop.models.product import Product


admin.site.register(Category)
admin.site.register(Product)
