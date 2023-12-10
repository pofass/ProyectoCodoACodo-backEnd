from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_filter=("created",)
    list_display=("title", "price", "image")
    search_fields=("title",)




admin.site.register(Product, ProductAdmin)