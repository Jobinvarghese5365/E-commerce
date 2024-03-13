from django.db import models

# Create your models here.
class contactdb(models.Model):
    contact_name = models.CharField(max_length=50, null=True, blank=True)
    contact_email = models.EmailField(max_length=50, null=True, blank=True)
    contact_subject = models.CharField(max_length=50, null=True, blank=True)
    contact_message = models.CharField(max_length=50, null=True, blank=True)

class registerdb(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email_id = models.EmailField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50,null=True,blank=True)

class cartdb(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Productname = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    TotalPrice = models.IntegerField(null=True,blank=True)