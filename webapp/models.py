from django.db import models

# Create your models here.
class ContactDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)
class  RegisterDb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    ConfirmPassword=models.CharField(max_length=100,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)

class CardDb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Total_price=models.IntegerField(null=True,blank=True)
    Product_name=models.CharField(max_length=100,null=True,blank=True)
    Prod_Image=models.ImageField(upload_to="Cart Images", null=True,blank=True)
class orderDb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Place=models.CharField(max_length=100,null=True,blank=True)
    Address=models.CharField(max_length=100,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)
    Total_price=models.IntegerField(null=True,blank=True)

