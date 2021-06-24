from django.contrib import admin

from products.models import Eav, Product, ProductAttribute, ProductAttributeValue

admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(Eav)
