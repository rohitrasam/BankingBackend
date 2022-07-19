from django.db.models import fields
from rest_framework import serializers
from .models import User, Accounts, Balance
from .user_model import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'ph_no', 'city', 'state', 'password')


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('debit', 'credit', 'total', 'account_no')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('account_no', 'account_type')

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'name', 'email', 'ph_no', 'city', 'state', 'accounts')