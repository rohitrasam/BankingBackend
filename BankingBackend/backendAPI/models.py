from django.db import models
from django.utils.timezone import now


# Create your models here.

today = now()
class BaseModel(models.Model):
    id = models.BigAutoField(auto_created=True ,primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    ph_no = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"



class Accounts(BaseModel):
    class Type(models.TextChoices):
        SAVINGS = "Savings"
        CURRENT = "Current"

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_account")
    account_no = models.CharField(unique=True, max_length=15)
    account_type = models.CharField(max_length=20, null=True, choices=Type.choices, default=Type.SAVINGS)

    def __str__(self):
        return f"{self.user_id} {self.account_no} {self.account_type}"


class Balance(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_balance")
    debit = models.DecimalField(decimal_places=4, max_digits=15, null=True)
    credit = models.DecimalField(decimal_places=4, max_digits=15, null=True)
    total = models.DecimalField(decimal_places=4, max_digits=15)
    account_no = models.ManyToManyField(Accounts, max_length=15)

    def __str__(self):
        return f"{self.user_id.full_name} {self.total}"

    
