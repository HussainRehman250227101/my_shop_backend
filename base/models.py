from django.db import models
from django.contrib.auth .models import User 

class Product(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True,blank=True)
    brand = models.CharField(max_length=200,null=True,blank=True)
    category = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    rating = models.DecimalField(max_digits=10, decimal_places=1 ,null=True, blank=True, default =0 )
    numReviews = models.IntegerField()
    price  =  models.DecimalField(max_digits=10, decimal_places=2 ,null=True, blank=True, default =0 )
    countInStock = models.IntegerField(null=True,blank=True)
    createdAt =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Review(models.Model):
    _id =  models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.DecimalField(max_digits=10, decimal_places=1 ,null=True, blank=True, default =0 )
    comment = models.TextField(null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.name) 
    

class Order(models.Model):
    _id =  models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(max_digits=10, decimal_places=2 ,null=True, blank=True )
    shippingPrice = models.DecimalField(max_digits=10, decimal_places=2 ,null=True, blank=True )
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2 ,null=True, blank=True )
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False) 
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False) 
    createdAt  = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.createdAt) 

class ShippingAddress(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    order = models.OneToOneField(Order,on_delete=models.CASCADE,null=True,blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=200, null=True,blank=True)
    postalCode = models.IntegerField(default=0, null=True,blank=True)
    country = models.CharField(max_length=200, null=True,blank=True)
    shippingPrice = models.DecimalField(max_digits=10, decimal_places=2 ,null=True, blank=True ) 

    def __str__(self):
        return str(self.order) 
    
class OrderItem(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True, blank = True)
    product =models.ForeignKey(Product,on_delete=models.CASCADE,null=True, blank = True)
    name = models.CharField(max_length=200, null=True,blank=True)
    qty = models.IntegerField(default=0, null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2 ,null=True, blank=True )
    image = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return str(f"{self.order} ------ {self.name} ")