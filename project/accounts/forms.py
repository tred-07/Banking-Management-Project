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
        fields=['username','password1','password2','first_name','last_name','email','birth_date','gender','street_address','city','postal_code','country']

    def save(self,commit=True):
        our_user=super().save(commit=False)
        if(commit==True):
            our_user.save() # save data user model
            account_type=self.cleaned_data('account_type')
            birth_date=self.cleaned_data.get('birth_date')
            gender=self.cleaned_data.get('gender')
            street_address=self.cleaned_data.get('street_address')
            city=self.cleaned_data('city')
            postal_code=self.cleaned_data('postal_code')
            country=self.cleaned_data('country') 
            UserAddress.objects.create(
                user=our_user,
                street_address=street_address,
                postal_code=postal_code,
                country=country,
            )
            UserBankModel.objects.create(
                user=our_user,
                account_no=1000+our_user.id,
                account_type=account_type,
                birth_date=birth_date,
                gender=gender,
                city=city
            )
        return our_user