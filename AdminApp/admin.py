from django.contrib import admin
from AdminApp.models import Categories,Product

class CategoriesAdmin(admin.ModelAdmin):
    list_display=('id','name')


class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','brand','price','details','image','category')

admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Product,ProductAdmin)