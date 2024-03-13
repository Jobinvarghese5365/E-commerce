from django.db import models

# Create your models here.
class categorydb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=50,null=True,blank=True)
    Image = models.ImageField(upload_to='image', null=True, blank=True)

class productdb(models.Model):
    Category_name = models.CharField(max_length=100,null=True,blank=True)
    Product_name = models.CharField(max_length=50,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Description = models.CharField(max_length=50,null=True,blank=True)
    Product_image = models.ImageField(upload_to='image', null=True, blank=True)