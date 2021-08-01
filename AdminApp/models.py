from django.db import models
from django.db.models.base import Model

class Categories(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20,default=0)
    price = models.FloatField(max_length=20)
    details = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Images")
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table="Products"