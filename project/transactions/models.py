from django.db import models
from accounts.models import UserBankModel
from .constants import TRANSACTION_TYPE
class Transction(models.Model):
    account=models.ForeignKey(UserBankModel,related_name="transactions",on_delete=models.CASCADE)
    amount=models.DecimalField(decimal_places=2,max_digits=12)
    balance_after_transaction=models.DecimalField(decimal_places=2,max_digits=12)
    transaction_type=models.IntegerField(choices=TRANSACTION_TYPE,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    loan_approve=models.BooleanField(default=False)

    class Meta:
        ordering=['timestamp'] # for sorting transactions

