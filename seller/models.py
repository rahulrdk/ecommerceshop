from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

from common.models import Seller

# Create your models here.

class Product(models.Model):
    seller = models.ForeignKey(Seller ,on_delete = models.CASCADE)
    p_name = models.CharField(max_length = 50)
    p_number = models.BigIntegerField()
    p_description = models.CharField(max_length = 300)
    p_price = models.IntegerField()
    p_stock =  models.IntegerField()
    p_image = models.ImageField(upload_to = 'products/')
