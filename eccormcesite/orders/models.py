from django.db import models
from product.models import Product 

# Create your models here.

class  Orders(models.Model):
    full_name    =   models.CharField(max_length=250)
    email        =   models.EmailField(unique=False)
    address      =   models.CharField(max_length=250)
    created_at   =   models.DateTimeField(auto_now_add=True)
    updated_at   =   models.DateTimeField(auto_now=True)
    paid         =   models.BooleanField(default=False)


    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order   =   models.ForeignKey(Orders,on_delete=models.CASCADE,related_name='items')
    product =   models.ForeignKey(Product,on_delete=models.CASCADE)
    price   =   models.DecimalField(max_digits=10,decimal_places=2)
    quantity =  models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity
