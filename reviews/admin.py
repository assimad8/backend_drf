from django.contrib import admin
from .models import Product,ProductSite,ProductSize,Category,Comment,Company,Image

# Register your models here.  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk','name','content')
    list_filter = ('category',)
admin.site.register(ProductSite)

admin.site.register(ProductSize)

admin.site.register(Category)

admin.site.register(Comment)

admin.site.register(Company)

admin.site.register(Image)

admin.site.site_header = "Product Review Admin"