from django.db import models
from AdminApp.models import Categories,Product

class UserInfo(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    email = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20,blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    phone = models.CharField(max_length=13,blank=True)
    occupation = models.CharField(max_length=20,blank=True)
    address = models.TextField(max_length=200,blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table="Userinfo"

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    message = models.TextField(max_length=200,blank=True)

    def __str__(self):
        return self.email
    
    class Meta:
        db_table="ContactUs"


class EmailUsers(models.Model):
    email = models.EmailField(max_length=30)
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'PasswordReset'
