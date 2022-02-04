from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    account_number=models.CharField(max_length=16,primary_key=True)
    phone=models.CharField(max_length=12,unique=True)
    pan=models.CharField(max_length=20,unique=True)
    mpin=models.CharField(max_length=6,unique=True)
    ac_type=models.CharField(max_length=12)
    balance=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.account_number
class Transactions(models.Model):
    account=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name="from_account")
    to_acno=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name="to_account")
    amount=models.PositiveIntegerField()
    date=models.DateField(auto_now_add=True)
    description=models.CharField(max_length=120)
    payment_mode=models.CharField(max_length=120) # choices g-pay,phone pay


