from django.contrib import admin

from categories.models import Category

from mptt.admin import MPTTModelAdmin

# admin.site.register(Category)
admin.site.register(Category , MPTTModelAdmin) 