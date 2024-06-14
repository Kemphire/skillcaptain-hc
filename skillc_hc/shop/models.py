from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    CATEGORIES = (
        ("cosmetics","beauty product"),
        ("stationery","study product"),
    )

    category = models.CharField(max_length=250,choices=CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name = } : {self.price = }"
    
class ProductStore(models.Model):
    store = models.ForeignKey(Shop,on_delete=models.CASCADE,related_name="store_of_product")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product")


