from django.contrib import admin
from .models import Category, Product, ProductAttribute, ProductAttributeValue
from mptt.admin import MPTTModelAdmin


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute

class CategoryAdmin(MPTTModelAdmin):
    inlines = [
        ProductAttributeInline
    ]

admin.site.register(Category, CategoryAdmin)

class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductAttributeValueInline
    ]

admin.site.register(Product, ProductAdmin)