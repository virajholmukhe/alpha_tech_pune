from django.db import models
from Accounts.models import UserInfo
from AdminApp.models import Categories,Product

class MyCart(models.Model):
    user = models.ForeignKey(UserInfo,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table = "MyCart"

class CustBuild(models.Model):
    user = models.ForeignKey(UserInfo,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = "CustBuild"

