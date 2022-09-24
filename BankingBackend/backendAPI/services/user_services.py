from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, serializers
from ..models import User, Accounts, Balance
from ..serializers import *
from django.contrib.auth.models import auth
from ..user_model import UserModel



def get_users():
    
    users = User.objects.all()
    user_list = [UserModel(
        user.id, 
        user.full_name, 
        user.email, 
        user.ph_no, 
        user.city, 
        user.state, 
        AccountSerializer(Accounts.objects.filter(user_id=user.id), many=True).data) 
        for user in users]

    if users:
        user_data = UserModelSerializer(user_list, many=True)
        return Response(user_data.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


def add_user(request: Request):
    try:
        if User.objects.filter(**request.data).exists():
            return Response("User already exists", status=status.HTTP_409_CONFLICT)

        user = UserSerializer(data=request.data)
        if user.is_valid():

            user.save()
            return Response("Account created", status=status.HTTP_200_OK)
    except:
        return Response("Failed to create account", status=status.HTTP_400_BAD_REQUEST)


def login(request: Request):

    email = request.data['email']
    password = request.data['password']
    try:
        user_data = User.objects.get(email=email)
        if password != user_data.password:
            return Response(data="Wrong password", status=status.HTTP_404_NOT_FOUND)
        if user_data is not None and not user_data.is_deleted:
            user = UserModelSerializer(user_data)
            return Response(user.data, status=status.HTTP_200_OK)
    except:
        return Response(data="User not found", status=status.HTTP_404_NOT_FOUND)


def get_user_details(id: int):

    try:
        user_data = User.objects.get(id=id)
        if user_data:
            user = UserModelSerializer(user_data)
            return Response(user.data, status=status.HTTP_200_OK)
    except:
        return Response("User not found", status=status.HTTP_400_BAD_REQUEST)


def update_user_info(request: Request, id: int):
    try:
        user_data = User.objects.get(id=id)
        if request.data['password'] == "" or request.data['password'] is None:
            request.data['password'] = user_data.password

        updated_user = UserSerializer(instance=user_data, data=request.data)

        if updated_user.is_valid():
            updated_user.save()
            return Response("User info updated successfully", status=status.HTTP_200_OK)
    except:
        return Response("Failed to update info", status=status.HTTP_400_BAD_REQUEST) 


def get_accounts(id: int):
    try:
        user_data = User.objects.get(id=id)
        accounts_data = user_data.user_account.all()
        print(accounts_data)
        if accounts_data.count() > 0:
            accounts = AccountSerializer(accounts_data, many=True)
            return Response(accounts.data, status=status.HTTP_200_OK)    
        return Response("No accounts found", status=status.HTTP_404_NOT_FOUND)
    except:
        return Response("User not found", status=status.HTTP_404_NOT_FOUND)
    
