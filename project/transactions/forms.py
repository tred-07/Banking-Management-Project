from django import forms
from .models import Transction
class TransactionForm(forms.ModelForm):
    class Meta: # used for extra characteristics
        model=Transction
        fields=['amount','transaction_type']

    def __init__(self,*args,**kwargs):
        self.account=kwargs.pop('account')
        super().__init__(*args,**kwargs)
        self.fields['transactions'].disabled=True # this field will be disabled
        self.fields['transactions'].widget=forms.HiddenInput() # hide from user
    
    def save(self,commit=True):
        self.instance.account=self.account
        self.instance.balance_after_transaction=self.account.balance
        return super().save()