from django.db import models

# Create your models here.

class Laptop(models.Model):
    company = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    price = models.IntegerField()