from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE,GENDER
# Create your models here.

class UserBankModel(models.Model):
    user=models.OneToOneField(User,related_name="account",on_delete=models.CASCADE)
    account_type=models.CharField(max_length=10,choices=ACCOUNT_TYPE)
    account_no=models.IntegerField(unique=True)
    birth_date=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=10,choices=GENDER)
    initilal_deposit_date=models.DateField(auto_now_add=True)# auto select date when deposit completed
    balance=models.DecimalField(max_digits=12,default=0,decimal_places=2)

    def __str__(self):
         return f'{self.account_no} {self.user}'

class UserAddress(models.Model):
     user=models.OneToOneField(User,related_name="address",on_delete=models.CASCADE)
     street_address=models.CharField(max_length=100)
     city=models.CharField(max_length=100)
     postal_code=models.IntegerField()
     country=models.CharField(max_length=40)
