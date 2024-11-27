from django.db import models

# Create your models here.
class Category_Db(models.Model):
    Category_Name=models.CharField(max_length=100,null=True,blank=True)
    Description= models.CharField(max_length=100, null=True, blank=True)
    Category_Image=models.ImageField(upload_to="Category_Images",null=True,blank=True)
class Product_Db(models.Model):
    Category=models.CharField(max_length=100,null=True,blank=True)
    Product_name=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True, blank=True)
    MRP=models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Country=models.CharField(max_length=100,null=True,blank=True)
    Manufactured=models.CharField(max_length=100,null=True,blank=True)
    Product_Image1 = models.ImageField(upload_to="Product_Images", null=True, blank=True)
    Product_Image2 = models.ImageField(upload_to="Product_Images", null=True, blank=True)
    Product_Image3 = models.ImageField(upload_to="Product_Images", null=True, blank=True)

