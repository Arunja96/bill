from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    del_flag = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True,null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True)
    rate = models.FloatField()
    select = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True,null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.product_name
    
class Bill(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    total_amount = models.FloatField(blank=True,null=True)
    product_ids = models.ManyToManyField(Product,blank=True)

    created_at = models.DateTimeField(auto_now_add=True,null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
class BillItem(models.Model):

    
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    product_name = models.CharField(max_length=100,blank=True,null=True)
    qty = models.FloatField(blank=True,null=True)
    rate = models.FloatField(blank=True,null=True)
    total = models.FloatField(blank=True,null=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self):
        return self.product_name
    

class BillSequence(models.Model):
    prefix = models.CharField(max_length=100)
    digi = models.IntegerField()
    after = models.BigIntegerField()

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

