from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Customer(models.Model):
    cust_name = models.CharField(max_length=40)
    cust_email = models.CharField(max_length=50)
    cust_phone = models.BigIntegerField()
    cust_image = models.ImageField(upload_to='customer/')
    cust_password = models.CharField(max_length=20)



class Seller(models.Model):
    seller_name = models.CharField(max_length=40)
    seller_email = models.CharField(max_length=50)
    seller_adds = models.CharField(max_length=100,default='')
    seller_phone = models.BigIntegerField()
    seller_accno = models.BigIntegerField(default=0)
    seller_ifsc = models.CharField(max_length=30,default='')
    seller_image = models.ImageField(upload_to='seller/')
    seller_password = models.CharField(max_length=20)
    seller_status = models.CharField(max_length=20,default = 'pending')


class Admin(models.Model):
    admin_id = models.IntegerField()
    admin_password = models.CharField(max_length=20)
    






