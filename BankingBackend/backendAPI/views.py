from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .services.user_services import *


# Create your views here.

# Gets all the users
@api_view(['GET'])
def get_all_users(request: Request):

    users = get_users()
    if users.status_code == 200:
        return Response(users.data, status=users.status_code)
    return Response(status=users.status_code)

# Create new users
@api_view(['POST'])
def create_user(request: Request):

    res = add_user(request)
    if res.status_code == 200:
        return Response(res.data, status=res.status_code)
    return Response(res.status_code)

# Validates and logs in user
@api_view(['POST'])
def login_user(request: Request):

    res = login(request)
    return Response(res.data, status=res.status_code)

# Get one user
@api_view(['GET'])
def get_user(request: Request, id: int):

    user = get_user_details(id)
    if user.status_code == 200:
        return Response(user.data, status=user.status_code)
    return Response(status=user.status_code)
    
@api_view(['PATCH'])
def update_user(request: Request, id: int):

    res = update_user_info(request, id)

    return Response(data=res.data, status=res.status_code)



# @api_view(['GET'])
# def get_accounts(request: Request, name: str, password: str):
#     user = User.objects.get(full_name=name, password=password)
#     accounts = Accounts.objects.filter(user_id=user.id)

#     if accounts and user:
#         acc_data = AccountSerializer(accounts, many=True)
#         user_data = UserModel(user.id,
#             user.full_name, user.email, user.ph_no,
#             user.city, user.state, acc_data.data)
#         user = UserModelSerializer(user_data)
#         return Response(user.data, status=status.HTTP_200_OK)
#     return Response(status=status.HTTP_404_NOT_FOUND)
