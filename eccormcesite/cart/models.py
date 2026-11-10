from django.db import models

from product.models import Product

class Cart(models.Model):
    created_at  =   models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

    

class CartItem(models.Model):
    cart        =   models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product     =   models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity    =   models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity
    



