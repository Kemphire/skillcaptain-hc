from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=260,unique=True)
    mobile_no = models.IntegerField(default=0)
    address = models.CharField(max_length = 500,default=f"Adress of person {name}")
    email = models.CharField(max_length=255,unique = True,null=True)
    def __str__(self):
        return f"Name: {self.name}, Mobile: {self.mobile_no}, Address: {self.address}"
