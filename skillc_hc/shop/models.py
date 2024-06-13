from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length = 250)
    address = models.TextField(blank = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    description = models.TextField(null = True, blank = True)
    category = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    shops = models.ManyToManyField(Shop)

    def __init__(self):
        return f"{self.name = } : {self.price = }"
    
