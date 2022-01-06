from django.contrib import admin
from django.db import models
from .models import Cart, CartItem
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_diplay =('cart_id', 'date_added',)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_activate')
    

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
