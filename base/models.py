from django.db import models
from django.contrib.auth .models import User 

class Product(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    # image 
    brand = models.CharField(max_length=200,null=True,blank=True)
    category = models.CharField(max_length=200,null=True,blank=True)
    descrition = models.TextField(null=True,blank=True)
    rating = models.DecimalField(max_digits=10, decimal_places=2 ,null=True, blank=True, default =0 )
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
    rating = models.DecimalField(max_digits=10, decimal_places=2 ,null=True, blank=True, default =0 )
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