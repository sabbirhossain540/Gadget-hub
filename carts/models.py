from django.db import models
#from carts.models import Cart
from store.models import Product

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, models.CASCADE)
    quantity = models.IntegerField()
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return self.product