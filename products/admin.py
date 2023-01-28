from django.contrib import admin

from products.models import ProductCategory, Poduct

admin.site.register(Poduct)  #  registry
admin.site.register(ProductCategory)
