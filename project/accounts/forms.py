from django.contrib.auth.forms import UserCreationForm
from .constants import GENDER,ACCOUNT_TYPE
from .models import UserBankModel,UserAddress
from django import forms
from django.contrib.auth.models import User
class UserRegistrationForm(UserCreationForm):
    birth_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender=forms.CharField(max_length=10,choices=GENDER)
    street_address=forms.CharField(max_length=100)
    city=forms.CharField(max_length=100)
    postal_code=forms.IntegerField()
    country=forms.CharField(max_length=40)
    class Meta:
        model=User
        fields=['username','password1','password2','first_name','last_name','email']
