from django.db import models
import datetime

# Create your models here.
class SaleItem(models.Model):
    # dateSold = models.DateField()
    numberSold = models.IntegerField()
    productSold = models.TextField()
    # payoutValue = models.FloatField()
