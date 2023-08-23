from django.contrib import admin
from products.models import Product, ProductsCategory
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductsCategory)
