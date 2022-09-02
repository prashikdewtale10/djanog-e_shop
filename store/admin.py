from django.contrib import admin

# Register your models here.
from .models import Product , Category , Customer , Order

#customing admin panel

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

class AdminCustomer(admin.ModelAdmin):
    list_display=['first_name','last_name']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory )
admin.site.register(Customer , AdminCustomer)
admin.site.register(Order)