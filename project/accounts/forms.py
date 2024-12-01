from django.contrib.auth.forms import UserCreationForm
from .constants import GENDER,ACCOUNT_TYPE
from .models import UserBankModel,UserAddress
from django import forms
from django.contrib.auth.models import User
class UserRegistrationForm(UserCreationForm):
    birth_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender=forms.ChoiceField(choices=GENDER)
    street_address=forms.CharField(max_length=100)
    city=forms.CharField(max_length=100)
    postal_code=forms.IntegerField()
    country=forms.CharField(max_length=40)
    account_type=forms.ChoiceField(choices=ACCOUNT_TYPE)
    class Meta:
        model=User
        fields=['username','password1','password2','first_name','last_name','email','birth_date','gender','street_address','city','postal_code','country']

    def save(self,commit=True):
        our_user=super().save(commit=True)
        if(commit==True):
            our_user.save() # save data user model
            account_type=self.cleaned_data.get('account_type')
            birth_date=self.cleaned_data.get('birth_date')
            gender=self.cleaned_data.get('gender')
            street_address=self.cleaned_data.get('street_address')
            city=self.cleaned_data.get('city')
            postal_code=self.cleaned_data.get('postal_code')
            country=self.cleaned_data.get('country') 
            UserAddress.objects.create(
                user=our_user,
                street_address=street_address,
                postal_code=postal_code,
                country=country,
                city=city
            )
            UserBankModel.objects.create(
                user=our_user,
                account_no=1000+our_user.id,
                account_type=account_type,
                birth_date=birth_date,
                gender=gender,
                
            )
        return our_user
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    'class':
                    (
                        'appearance-none block w-full bg-gray-600'
                        'text-gray-700 border border-gray-200 rounded'
                        'py-[10px] px-[10px] leading-tight focus:outline-none'
                        'focus:bg-white focus:border-gray-500'
                    )
                }
            )


class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
        # jodi user er account thake 
        if self.instance:
            try:
                user_account = self.instance.account
                user_address = self.instance.address
            except UserBankModel.DoesNotExist:
                user_account = None
                user_address = None

            if user_account:
                self.fields['account_type'].initial = user_account.account_type
                self.fields['gender'].initial = user_account.gender
                self.fields['birth_date'].initial = user_account.birth_date
                self.fields['street_address'].initial = user_address.street_address
                self.fields['city'].initial = user_address.city
                self.fields['postal_code'].initial = user_address.postal_code
                self.fields['country'].initial = user_address.country

    def save(self, commit=True):
        user = super().save(commit=True)
        if commit:
            user.save()

            user_account, created = UserBankModel.objects.get_or_create(user=user) # jodi account thake taile seta jabe user_account ar jodi account na thake taile create hobe ar seta created er moddhe jabe
            user_address, created = UserAddress.objects.get_or_create(user=user) 

            user_account.account_type = self.cleaned_data['account_type']
            user_account.gender = self.cleaned_data['gender']
            user_account.birth_date = self.cleaned_data['birth_date']
            user_account.save()

            user_address.street_address = self.cleaned_data['street_address']
            user_address.city = self.cleaned_data['city']
            user_address.postal_code = self.cleaned_data['postal_code']
            user_address.country = self.cleaned_data['country']
            user_address.save()

        return user