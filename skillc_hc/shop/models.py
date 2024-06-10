from django.db import models


class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    description = models.TextField(null = True, blank = True)
    category = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)

    def __init__(self):
        return f"{self.name = } : {self.price = }"