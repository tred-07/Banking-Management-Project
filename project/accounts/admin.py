from django.contrib import admin
from .models import UserAddress,UserBankModel
# Register your models here.
admin.site.register(UserAddress)
admin.site.register(UserBankModel)