from django.contrib import admin
from .models import Product

admin.site.site_header = "My Shop Admin"
admin.site.site_title = "My Shop Admin Portal"
admin.site.index_title = "Welcome to My Shop Administration"

def mark_as_out_stock(modeladmin, request, queryset):
    queryset.update(stock=0)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','description','stock')
    list_editable =('price', 'stock')
    search_fields = ('name','description')
    actions = [mark_as_out_stock]
    list_per_page = 10


# Register your models here.
admin.site.register(Product, ProductAdmin)
