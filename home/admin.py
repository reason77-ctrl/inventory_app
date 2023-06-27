from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','image','date_field']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','fa_image']


admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
